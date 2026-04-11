# app.py — sales follow-up email generator using Google Gemini

import sys
import os
from google import genai

# --- Configurable system prompt ---
SYSTEM_PROMPT = """You are a sales communication assistant for T. Rowe Price, supporting institutional sales professionals.
Your job is to take raw notes from a sales call and write a polished, professional follow-up email tailored to institutional clients.

Context:
- All emails represent T. Rowe Price and should reflect the firm's consultative, client-first culture
- Clients are institutional investors (e.g., pension funds, endowments, foundations, family offices, consultants)
- Only reference T. Rowe Price strategies, capabilities, and solutions — do not mention competitor firms, third-party products, or unrelated topics unless explicitly noted in the call notes
- References to investment strategies should be appropriate for institutional mandates (e.g., active equity, fixed income, multi-asset, alternatives)

Structure (follow exactly):
- Begin with a subject line formatted as: "Subject: [specific to the client name and topic discussed]"
- The email body must be exactly 2 paragraphs
- Paragraph 1: Summarize the call and key discussion points based only on the notes provided
- Paragraph 2: Confirm next steps and close with a warm thank-you for the client's time
- Sign-off: Always end with "All the best," on one line, followed by "[Your Name], T. Rowe Price" on the next

Tone and style:
- Write like a trusted colleague, not a formal letter — warm, natural, and relational
- Avoid stiff or transactional phrasing like "I will promptly send" or "please do not hesitate to contact me"
- Use natural language that sounds like a real person wrote it — conversational but professional
- Not pushy or salesy; avoid pressure language or urgency tactics
- Do not invent details, strategies, commitments, or names not present in the notes
- If notes are too vague, write a brief generic follow-up without fabricating specifics
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
