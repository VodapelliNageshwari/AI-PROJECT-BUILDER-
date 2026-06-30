# mini_project_agent/agent.py

import os
from generator import generate_project_assets

def main():
    """
    Main function to run the project generation agent.
    """
    print("=============================================")
    print("🚀 Welcome to the AI MEGA PROJECT BUILDER 🚀")
    print("=============================================")
    
    domain = input("Enter the project domain (e.g., AI Voice Assistant, Web App, IoT System): ").strip()
    language = input("Enter the preferred programming language (e.g., Python, Java, JavaScript): ").strip()

    if not domain or not language:
        print("❌ Domain and language cannot be empty. Exiting.")
        return

    print(f"\n⏳ Generating a '{domain}' project in {language.title()}. Please wait...\n")

    try:
        project_title, _ = generate_project_assets(domain, language)
        print(f"\n🎉 Successfully generated project in: output/{project_title}")
    except Exception as e:
        print(f"\n❌ An error occurred during project generation: {e}")
        print("Please check your .env file for a valid GROQ_API_KEY and your network connection.")

if __name__ == "__main__":
    main()