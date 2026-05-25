# 📊 Pipeline de Análise de Sentimento para Suporte ao Cliente (Deep Learning)

Este projeto implementa um pipeline inteligente de classificação de chamados de suporte. Ele utiliza técnicas avançadas de Processamento de Linguagem Natural (NLP) para automatizar a triagem de mensagens de clientes.

## 🚀 Arquitetura do Sistema

1. **Camada de IA (Deep Learning):** Integração com modelos baseados em **Transformers (BERT)** via ecossistema Hugging Face, especializado na extração de contexto e análise de sentimento em português.
2. **Engenharia de Dados:** Armazenamento automático de logs, mensagens analisadas e escores de confiança em um banco de dados relacional **SQLite**.
3. **Engenharia de IA (API):** Construção de endpoints assíncronos e de alta performance utilizando **FastAPI** para disponibilizar as predições.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem Principal:** Python
* **Processamento de Linguagem Natural:** Hugging Face (Transformers), PyTorch
* **Engenharia de Software & API:** FastAPI, Uvicorn, Pydantic
* **Análise & Banco de Dados:** Pandas, SQLite3
