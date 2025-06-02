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
    # TAREFA 1: escolher o modelo apropriado e ajustar entrada do usuário

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="ENTER_INPUT_HERE"),
            ],
        ),
    ]
    tools = [
        types.Tool(google_search=types.GoogleSearch()), # O modelo usa Google Search como Ferramenta adicional
    ]
    generate_content_config = types.GenerateContentConfig(
        tools=tools,
        response_mime_type="text/plain",
    )

    resposta=""

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        resposta+=chunk.text
    return resposta

#if __name__ == "__main__":
#    # Teste para ter certeza que funciona
#    test_response = generate(entrada="Olá, como está o tempo hoje em Cuiabá?")
#    print(f"Test response: {test_response}")