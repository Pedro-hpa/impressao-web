from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Configuração de diretórios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_DIR = os.path.join(BASE_DIR, "static/pdfs")
SPRINTER_DIR = os.path.join(BASE_DIR, "static/sprinter")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/") # Listar pdf caminhao
def listar_pdfs(request: Request):
    arquivos = [f for f in os.listdir(PDF_DIR) if f.endswith(".pdf")]
    return templates.TemplateResponse("index.html", {
        "request": request,
        "arquivos": arquivos
    })

@app.get("/sprinter") # Listar pdf sprinter
def listar_sprinter(request: Request):
    arquivos = [f for f in os.listdir(SPRINTER_DIR) if f.endswith(".pdf")]
    return templates.TemplateResponse("index.html", {
        "request": request,
        "arquivos": arquivos
    })

@app.get("/pdf/{arquivo}") # Pesquisa caminhao
def abrir_pdf(arquivo: str):
    caminho = os.path.join(PDF_DIR, arquivo)
    return FileResponse(caminho, media_type="application/pdf")

@app.get("/sprinter-pdf/{arquivo}") # Pesquisa caminhao
def abrir_pdf_sprinter(arquivo: str):
    caminho = os.path.join(SPRINTER_DIR, arquivo)
    return FileResponse(caminho, media_type="application/pdf")
