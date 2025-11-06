from googletrans import Translator
from langdetect import detect
from transformers import pipeline

# Translator and mock LLM
translator = Translator()
generator = pipeline("text2text-generation", model="google/flan-t5-base", tokenizer="google/flan-t5-base")

def detect_language(text: str) -> str:
    """Detect language (returns 'en' or 'ja' or other ISO code)."""
    return detect(text)

def translate_text(text: str, target_lang: str) -> str:
    """Translate text to target language."""
    return translator.translate(text, dest=target_lang).text

def generate_answer(prompt: str) -> str:
    """Generate mock LLM response."""
    return generator(prompt, max_length=256, truncation=True)[0]["generated_text"]
