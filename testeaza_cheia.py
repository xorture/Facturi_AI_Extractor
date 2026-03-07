import os
from dotenv import load_dotenv

load_dotenv()

cheia_mea = os.getenv("GEMINI_API_KEY")

if cheia_mea:
    print(f"Am gasit cheia! Are {len(cheia_mea)} de caractere")
else:
    print("Nu am gasit nimic, verifica fisierul .env.")