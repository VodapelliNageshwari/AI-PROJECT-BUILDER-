# mini_project_agent/formatter.py

import re

def parse_response(response_text: str):
    """
    Parses the LLM response into a dictionary of filenames and their content.

    Expected format:
    <<<filename>>>
    file content...
    <<<next_filename>>>
    next file content...
    """
    pattern = r"<<<(.+?)>>>\n(.*?)(?=\n<<<|$)"  # matches <<<filename>>> followed by content
    matches = re.findall(pattern, response_text, re.DOTALL)

    files = {}
    for filename, content in matches:
        files[filename.strip()] = content.strip()

    return response_text, files

