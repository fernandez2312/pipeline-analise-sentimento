import sqlite3

def inicializar_banco():
    conn = sqlite3.connect('suporte_dados.db')
    cursor = conn.cursor()
    
    # Tabela para auditoria e logs de chamados processados pela IA
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chamados_suporte (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto_mensagem TEXT,
            sentimento TEXT,
            score REAL,
            data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Banco de dados do suporte inicializado com sucesso!")

if __name__ == "__main__":
    inicializar_banco()
