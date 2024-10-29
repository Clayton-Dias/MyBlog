# Instala as dependências necessárias (execute no terminal AIzaSyDrbBo43I4NNiach_cOykLZxYoIcXzPqaA)
# pip install google-generativeai

import google.generativeai as genai
import os

# Defina a chave da API diretamente ou carregue de uma variável de ambiente
#GOOGLE_GEMINI_API_KEY = os.getenv('GOOGLE_GEMINI_API_KEY')  # ou defina manualmente

#if GOOGLE_GEMINI_API_KEY is None:
    #raise ValueError("A chave da API GOOGLE_GEMINI_API_KEY não está definida.")

# Configuração da API
genai.configure(api_key='')

# Listar os modelos disponíveis
for modelo in genai.list_models():
    if 'generateContent' in modelo.supported_generation_methods:
        print(modelo.name)

# Inicializar o modelo
modelo = genai.GenerativeModel("models/gemini-1.5-pro-latest")
chat = modelo.start_chat(history=[])

print("Bem-vindo ao Chat com Gemini! Digite 'sair' para encerrar.")

# Loop de interação com o usuário
while True:
    prompt = input("Digite sua pergunta: ")
    if prompt.lower() == "sair":
        break  # Sai do loop se o usuário digitar 'sair'

    response = chat.send_message(prompt)
    print(f"Gemini: {response.text}")  # Formatação mais clara da resposta
