# mini_project_agent/agent.py

import os
from generator import generate_project_assets
from utils import save_project

def main():
    domain = input("Enter domain (e.g., AI, Web, IoT, etc.): ").strip()
    language = input("Preferred programming language (Python, Java, etc.): ").strip()

    print("\n⏳ Generating project. Please wait...\n")

    project_title, response_text = generate_project_assets(domain, language)

    save_project(project_title, response_text)

    print(f"\n✅ Project saved successfully in output/{project_title}\n")

if __name__ == "__main__":
    main()
