# Chatbot de Clima - Desafio Técnico 20DASH

Este projeto implementa uma API em **Python + FastAPI** que funciona como chatbot.  
O bot responde perguntas gerais usando o modelo **meta-llama/llama-4-scout-17b-16e-instruct** da [Groq](https://console.groq.com/) e retorna **previsão do tempo** quando o usuário pergunta sobre clima.

---

## 🚀 Como rodar o projeto

### 1. Clonar o repositório
```bash
git clone <repo-url>
cd desafio-chatbot
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Definir variáveis de ambiente
```bash
export GROQ_API_KEY="sua_chave_groq"
export OPENWEATHER_API_KEY="sua_chave_openweather"
```

> ⚠️ Se estiver no Windows (PowerShell):
```powershell
$env:GROQ_API_KEY="sua_chave_groq"
$env:OPENWEATHER_API_KEY="sua_chave_openweather"
```

### 4. Rodar a API
```bash
uvicorn main:app --reload
```

A API estará disponível em:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📡 Endpoints

### `POST /`

#### Exemplo 1 - Pergunta normal
**Request**
```bash
curl http://127.0.0.1:8000 -s     -H "Content-Type: application/json"     -d '{"message": "Qual era a principal guitarra do Jimi Hendrix?"}'
```

**Response**
```json
{"response":"A principal guitarra do Jimi Hendrix era a Fender Stratocaster."}
```

---

#### Exemplo 2 - Pergunta sobre clima
**Request**
```bash
curl http://127.0.0.1:8000 -s     -H "Content-Type: application/json"     -d '{"message": "Vai chover em Bertioga amanhã?"}'
```

**Response**
```json
{"response":"A previsão do tempo em Bertioga é de mínima 20°C e máxima 24°C."}
```

---

## 🧪 Testes

Rodar os testes unitários com:
```bash
pytest
```

Os testes verificam:
1. Uma pergunta **não relacionada a clima**.
2. Uma pergunta **relacionada a clima**.
