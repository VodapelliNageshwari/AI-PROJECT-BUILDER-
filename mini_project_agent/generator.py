import os
from groq import Groq
from dotenv import load_dotenv
from templates import get_project_prompt_template
from utils import save_project

# Load environment variables from .env
load_dotenv()

# Initialize Groq client using API key from environment variables
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = Groq(api_key=api_key)

def generate_project_assets(domain: str, language: str):
    """
    Generates the full project structure by calling the LLM with a refined prompt.
    """
    prompt = get_project_prompt_template(domain, language)
    
    print("🤖 Calling AI model with advanced instructions... This may take a moment.")
    
    chat_response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,  # Lowered for more accurate and predictable code
        top_p=0.9,
    )

    project_text = chat_response.choices[0].message.content.strip()
    project_title = f"{domain.title().replace(' ', '_')}_{language.lower()}_project"

    print("✅ Project assets generated. Saving files...")
    save_project(project_title, project_text)
    return project_title, project_text