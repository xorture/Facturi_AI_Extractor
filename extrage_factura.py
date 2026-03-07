import os
import pdfplumber
from groq import Groq
from dotenv import load_dotenv

# 1. Deschidem seiful si luam parola
load_dotenv()
cheia_mea = os.getenv("GEMINI_API_KEY") # o ia direct pe aia de la Groq

# 2. Conectam noul creier (Clientul Groq)
client = Groq(api_key=cheia_mea)

# 3. Deschidem ochii (Citim PDF-ul)
fisier = "factura.pdf"
text_extras = ""

print("1. Citesc PDF-ul, stai asa...")
try:
    with pdfplumber.open(fisier) as pdf:
        for pagina in pdf.pages:
            text_extras += pagina.extract_text()
except FileNotFoundError:
    print(f"Eroare: Nu am gasit fisierul '{fisier}'. Pune o factura in folder!")
    exit()

# 4. Dam textul la AI si ii cerem JSON
prompt = f"""
Asta e textul extras de pe o factura: 
{text_extras}

Te rog sa extragi urmatoarele date: numele firmei (furnizorul care a emis factura), suma totala de plata si data facturii.
Raspunde STRICT in format JSON curat, fara marcaje markdown (fara ```json) sau alte explicatii. Fix asa:
{{"firma": "Numele Firmei SRL", "total": 150.50, "data": "DD.MM.YYYY"}}
"""

print("2. Trimit textul la noul AI (Groq) sa scoata datele...")

# Folosim modelul Llama-3 care e incredibil de rapid
raspuns = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama-3.3-70b-versatile", # Asta e singura linie modificata
)
# Printam ce a gasit AI-ul
print("\n--- REZULTAT FINAL ---")
print(raspuns.choices[0].message.content)