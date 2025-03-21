from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Configuração de diretórios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_DIR = os.path.join(BASE_DIR, "static/pdfs")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def listar_pdfs(request: Request):
    """Lista todos os PDFs disponíveis na pasta."""
    arquivos = [f for f in os.listdir(PDF_DIR) if f.endswith(".pdf")]
    return templates.TemplateResponse("index.html", {"request": request, "arquivos": arquivos})

@app.get("/pdf/{arquivo}")
def abrir_pdf(arquivo: str):
    """Abre um arquivo PDF específico."""
    caminho = os.path.join(PDF_DIR, arquivo)
    return FileResponse(caminho, media_type="application/pdf")
