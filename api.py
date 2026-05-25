from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
# Importa o motor de IA do arquivo que testamos
from classificador import analisar_texto 

app = FastAPI(title="Pipeline de Análise de Sentimento - Suporte")

# Define o formato de dados que a API espera receber (JSON)
class ChamadoEntrada(BaseModel):
    texto: str

def salvar_log_banco(texto, sentimento, score):
    conn = sqlite3.connect('suporte_dados.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO chamados_suporte (texto_mensagem, sentimento, score)
        VALUES (?, ?, ?)
    ''', (texto, sentimento, score))
    conn.commit()
    conn.close()

@app.get("/")
def index():
    return {"status": "API de Análise de Sentimento Ativa!"}

@app.post("/analisar")
def analisar_chamado(chamado: ChamadoEntrada):
    if not chamado.texto.strip():
        raise HTTPException(status_code=400, detail="O texto da mensagem nao pode estar vazio.")
    
    # 1. Processa o texto através do modelo de Deep Learning
    sentimento, confianca = analisar_texto(chamado.texto)
    
    # 2. Engenharia de Dados: Persiste o resultado no banco SQLite
    salvar_log_banco(chamado.texto, sentimento, confianca)
    
    # 3. Define uma regra de negócio / Automação (Alerta Prioritário)
    alerta_urgente = True if sentimento == "URGENTE / RECLAMACAO" else False
    
    return {
        "mensagem_original": chamado.texto,
        "classificacao_ia": sentimento,
        "score_confianca": round(float(confianca), 2),
        "disparar_alerta_suporte": alerta_urgente
    }
