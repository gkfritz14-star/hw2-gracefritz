# app.py — sales follow-up email generator using Google Gemini

import sys
import os
from google import genai

# --- Configurable system prompt ---
SYSTEM_PROMPT = """You are an expert sales communication assistant.
Your job is to take raw notes from a sales call and write a polished, professional follow-up email.

Guidelines:
- Thank the prospect sincerely but concisely for their time
- Summarize the key points discussed based only on the notes provided
- Clearly state any agreed-upon next steps
- Use a confident, professional, and warm tone — avoid being overly enthusiastic
- Do not invent details, names, numbers, or commitments that are not in the notes
- If the notes are too vague to produce a specific email, write a brief, generic follow-up and do not fabricate specifics
- Keep the email concise — no longer than necessary
"""

def load_notes(filepath):
    with open(filepath, "r") as f:
        return f.read().strip()

def generate_email(notes):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Here are the sales call notes:\n\n{notes}",
        config={"system_instruction": SYSTEM_PROMPT}
    )
    return response.text

def main():
    if len(sys.argv) != 2:
        print("Usage: python app.py <path_to_notes_file>")
        sys.exit(1)

    notes_file = sys.argv[1]

    if not os.path.exists(notes_file):
        print(f"Error: File '{notes_file}' not found.")
        sys.exit(1)

    notes = load_notes(notes_file)

    print("\n--- Raw Notes ---")
    print(notes)
    print("\n--- Generated Follow-Up Email ---\n")

    email = generate_email(notes)
    print(email)
    print("\n---------------------------------\n")

if __name__ == "__main__":
    main()
