import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def test_sentiment_analysis_with_IA(page):
    page.goto("https://automationexercise.com/products")
    page.wait_for_load_state("networkidle")

    page.get_by_role("link", name="View Product").first.click(force=True)
    page.get_by_placeholder("Add Review Here!").fill("I loved this product! The quality is amazing.")
    customer_comment = page.get_by_placeholder("Add Review Here!").input_value()
    answer_ia = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Analise o seguinte comentário de um cliente e responda apenas com uma palavra ('Positivo', 'Negativo' ou 'Neutro'): {customer_comment}"
    )
    result_feeling = answer_ia.text.strip()

    assert result_feeling == "Positivo"