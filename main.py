from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import Dict
import fitz  # PyMuPDF pour PDF
import docx2txt
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import spacy
import spacy.cli

spacy.cli.download("en_core_web_sm")


load_dotenv()

app = FastAPI()
nlp = spacy.load("en_core_web_sm")

# Initialiser client Groq LLM
llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model="compound-beta")

def extract_text_from_pdf(file_path: str) -> str:
    doc = fitz.open(file_path)
    return "\n".join(page.get_text("text") for page in doc)

def extract_text_from_docx(file_path: str) -> str:
    return docx2txt.process(file_path)

def simple_ats_checks(text: str) -> Dict:
    doc = nlp(text.lower())
    keywords = ["expérience", "compétences", "formation", "projet", "certification"]
    present_keywords = [kw for kw in keywords if kw in text.lower()]
    score = len(present_keywords) / len(keywords) * 100
    return {"keywords_found": present_keywords, "basic_score": round(score, 2)}

@app.post("/analyze_cv/")
async def analyze_cv(cv_file: UploadFile = File(...)) -> Dict:
    # Sauvegarder fichier temporaire
    file_ext = os.path.splitext(cv_file.filename)[1].lower()
    temp_path = f"temp_{cv_file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await cv_file.read())

    # Extraire texte
    if file_ext == ".pdf":
        text = extract_text_from_pdf(temp_path)
    elif file_ext in [".docx", ".doc"]:
        text = extract_text_from_docx(temp_path)
    else:
        os.remove(temp_path)
        raise HTTPException(status_code=400, detail="Format de fichier non supporté")

    os.remove(temp_path)

    # Analyse simple ATS
    basic_analysis = simple_ats_checks(text)

    # Construire prompt pour Groq LLM
    prompt = f"""
    Tu es un expert en ATS (Applicant Tracking Systems). Analyse ce CV et donne un diagnostic détaillé sur sa conformité aux règles ATS :
    - Structure claire et sections standard
    - Présence de mots-clés pertinents
    - Format adapté
    Donne un score sur 20 et des recommandations précises pour améliorer le CV.
    Voici le texte du CV :
    {text[:3000]}  # Limite la taille pour API
    """

    # Appel à l'API Groq
    response = llm.invoke(prompt)

    return {
        "basic_analysis": basic_analysis,
        "llm_diagnostic": response
    }
