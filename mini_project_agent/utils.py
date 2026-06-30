import os
import re
import unicodedata
from datetime import datetime

def slugify(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[\s_-]+', '_', text.strip())
    return text

def save_project(project_title, response_text):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = f"{slugify(project_title)}_{timestamp}"  # Make it unique
    project_folder = os.path.join("output", folder_name)
    os.makedirs(project_folder, exist_ok=True)

    current_file = None
    current_lines = []

    for line in response_text.splitlines():
        file_match = re.match(r'^\*\*<<<(.+?)>>>$', line.strip())
        if file_match:
            if current_file:
                save_file(project_folder, current_file, '\n'.join(current_lines))
            current_file = file_match.group(1).strip()
            current_lines = []
        else:
            if current_file:
                current_lines.append(line)

    if current_file:
        save_file(project_folder, current_file, '\n'.join(current_lines))

    print(f"✅ Project saved successfully in {project_folder}")

def save_file(base_path, relative_path, content):
    full_path = os.path.join(base_path, relative_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
