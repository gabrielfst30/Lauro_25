# To run this code you need to install the following dependencies:
# pip install google-genai

from dotenv import load_dotenv  # This is the new import you need

load_dotenv()

import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )
    # TAREFA 1: escolher o modelo apropriado e ajustar entrada do usuário e retorno da função


#if __name__ == "__main__":
#    # Teste para ter certeza que funciona
#    test_response = generate(entrada="Olá, como está o tempo hoje em Cuiabá?")
#    print(f"Test response: {test_response}")