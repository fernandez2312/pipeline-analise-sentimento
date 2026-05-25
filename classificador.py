from transformers import pipeline

print("Carregando o modelo de linguagem natural (NLP) em português... Aguarde.")

# Inicializa o pipeline de análise de sentimento com um modelo especializado em português
# Na primeira execução, o Python fará o download do modelo automaticamente (cerca de 500MB)
analisador = pipeline(
    "sentiment-analysis", 
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

def analisar_texto(texto):
    try:
        resultado = analisador(texto)[0]
        # O modelo retorna estrelas de 1 a 5. Vamos mapear para sentimentos de suporte comercial:
        label = resultado['label'] # Ex: "1 star", "5 stars"
        score = resultado['score'] # Confiança do modelo (0.0 a 1.0)
        
        if label in ["1 star", "2 stars"]:
            sentimento = "URGENTE / RECLAMACAO"
        elif label == "3 stars":
            sentimento = "NEUTRO"
        else:
            sentimento = "ELOGIO / SATISFEITO"
            
        return sentimento, score
    except Exception as e:
        print(f"Erro na análise do texto: {e}")
        return "ERRO", 0.0

if __name__ == "__main__":
    # Teste rápido de validação do motor de IA
    msg_teste = "Estou muito irritado, meu produto veio quebrado e ninguém me responde!"
    sent, conf = analisar_texto(msg_teste)
    print(f"\n[TESTE] Mensagem: '{msg_teste}'")
    print(f"[TESTE] Classificação da IA: {sent} (Confiança: {conf:.2f})")
