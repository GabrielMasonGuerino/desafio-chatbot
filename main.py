import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Configurações
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

class Message(BaseModel):
    message: str

def get_weather(city: str):
    """Consulta a previsão do tempo via OpenWeather API"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={OPENWEATHER_API_KEY}&lang=pt_br"
    resp = requests.get(url).json()
    if resp.get("cod") != 200:
        return f"Não consegui encontrar previsão para {city}."
    
    temp_min = resp["main"]["temp_min"]
    temp_max = resp["main"]["temp_max"]
    return f"A previsão do tempo em {city} é de mínima {temp_min}°C e máxima {temp_max}°C."

def ask_groq(prompt: str):
    """Consulta a API da Groq para identificar intenção"""
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    url = "https://api.groq.com/openai/v1/chat/completions"
    data = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
    }
    response = requests.post(url, headers=headers, json=data).json()
    return response["choices"][0]["message"]["content"]

@app.post("/")
async def chatbot(msg: Message):
    user_message = msg.message

    # Pergunta para o LLM se é sobre clima
    check_prompt = f"O usuário disse: '{user_message}'. Isso é uma pergunta sobre previsão do tempo? Responda apenas com SIM ou NÃO."
    llm_response = ask_groq(check_prompt).strip().upper()

    if "SIM" in llm_response:
        # tenta extrair cidade
        city_prompt = f"Extraia o nome da cidade do texto: '{user_message}'. Responda apenas com a cidade."
        city = ask_groq(city_prompt).strip()
        weather = get_weather(city)
        return {"response": weather}
    else:
        # resposta normal do bot
        return {"response": ask_groq(user_message)}
