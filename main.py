from fastapi import FastAPI, Request
from pydantic import BaseModel
import os
import platform
import requests

app = FastAPI()

PASTA_PDFS = "pdfs"  # Pasta onde os PDFs baixados serão salvos
os.makedirs(PASTA_PDFS, exist_ok=True)

class ImprimirRequest(BaseModel):
    nome: str

@app.post("/imprimir")
def imprimir_arquivo(dados: ImprimirRequest):
    url_pdf = f"https://impressao-web.onrender.com/pdf/{dados.nome}"
    caminho_local = os.path.join(PASTA_PDFS, dados.nome)

    try:
        # Baixar o PDF da nuvem
        resposta = requests.get(url_pdf)
        with open(caminho_local, "wb") as f:
            f.write(resposta.content)

        # Imprimir (somente no Windows com Adobe/Reader padrão)
        if platform.system() == "Windows":
            os.startfile(caminho_local, "print")
            return {"status": "Impressão enviada"}

        return {"erro": "Impressão automática só implementada para Windows"}

    except Exception as e:
        return {"erro": str(e)}