# mini_project_agent/templates.py

def get_project_prompt_template(domain: str, language: str) -> str:
    return f"""
You are an expert-level, senior software architect and B.Tech project development specialist.

Your task is to generate a **complete, production-grade, and fully functional final-year B.Tech project** in the domain of "{domain}" using the language "{language}". The project must be ready to be cloned, built, and run without any modifications.

**⚠️ CRITICAL REQUIREMENTS ⚠️**:
- **NO PLACEHOLDERS:** All functions, methods, and classes must be **fully implemented**. Code must not contain any placeholders like `// ...`, `pass`, `// TODO`, or similar markers of incomplete logic.
- **SELF-CONTAINED & RUNNABLE:** The project must work out-of-the-box. For ML/AI projects, this means the main script must automatically trigger model training if the necessary model files (`.pkl`, `.h5`, etc.) are not found.
- **EMBEDDED TRAINING DATA:** The training script itself must contain the necessary training data (e.g., in an array or list of tuples). Do not rely on external `.csv` files for training.
- **CONFIGURATION & SECRETS:** All configuration variables (e.g., API endpoints) and secrets (e.g., API keys) **MUST** be loaded from the `.env` file via the `modules/config` module.
- **ROBUST ERROR HANDLING:** Implement comprehensive and specific error handling for all I/O operations, API calls, and potential runtime errors.

**PROJECT STRUCTURE TO FOLLOW (Strictly):**

1.  `<<<README.md>>>` – Comprehensive project overview, features, and detailed setup instructions.
2.  `<<<main.{get_file_extension(language)}>>>` – The main entry point. **Must include logic to check for model artifacts and run training if they are missing.**
3.  `<<<train_model.{get_file_extension(language)}>>>` – (If ML/AI) The script to train the model and save artifacts. **Must contain the training data.**
4.  `<<<modules/core_logic.{get_file_extension(language)}>>>` – The central business logic.
5.  `<<<modules/ui.{get_file_extension(language)}>>>` – Code for the user interface.
6.  `<<<modules/config.{get_file_extension(language)}>>>` – Handles loading configuration from environment variables.
7.  `<<<{get_dependencies_filename(language)}>>>` – The complete list of project dependencies with versions.
8.  `<<<.env>>>` – A template for environment variables with clear placeholders.
9.  `<<<tests/test_main.{get_file_extension(language)}>>>` – Comprehensive, mocked unit tests.
10. `<<<report.md>>>` – A detailed project report.
11. `<<<ppt.md>>>` – A slide-by-slide presentation structure.
12. `<<<resume.txt>>>` – Bullet points for a resume.

**Final Instructions:**
- Wrap each filename exactly in `<<<filename>>>`.
- Provide all source code in ```{language} code blocks.
- Do not add any commentary outside the requested files.
"""


def get_file_extension(language: str) -> str:
    ext_map = {
        "python": "py",
        "java": "java",
        "javascript": "js",
    }
    return ext_map.get(language.lower(), "txt")

def get_dependencies_filename(language: str) -> str:
    dep_map = {
        "python": "requirements.txt",
        "java": "pom.xml",
        "javascript": "package.json",
    }
    return dep_map.get(language.lower(), "dependencies.txt")