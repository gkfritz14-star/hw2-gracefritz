# Report: AI-Generated Sales Follow-Up Emails for T. Rowe Price Institutional Sales

---

## Use Case

T. Rowe Price institutional sales professionals manage large books of prospects and clients across pension funds, endowments, foundations, and family offices. After each meeting or call, reps are expected to send timely, polished follow-up emails that recap the conversation and confirm next steps. In practice, this is time-consuming — especially for reps traveling between meetings — and quality varies significantly across the team.

This prototype addresses that gap by taking raw, unstructured post-call notes and generating a professional follow-up email using the Gemini API. The goal is not to fully automate the process, but to give reps a strong, personalized first draft they can quickly review and send.

---

## Model Selection: Gemini 2.5 Flash

The prototype was built and tested using Google's Gemini API. During development, both `gemini-2.0-flash` and `gemini-1.5-flash` were attempted but returned 404 errors, as these models are no longer available to new API users. `gemini-2.5-pro` was also tested but returned persistent 503 overload errors throughout the session. `gemini-2.5-flash` was the model that ultimately worked reliably and produced high-quality output, making it the clear choice for this use case. It also represents the current generation of Gemini Flash models, offering a strong balance of speed, quality, and availability for a task like this.

---

## Prompt Development: Baseline to Final

Three prompt versions were developed and documented in `prompts.md`.

**Version 1 (Baseline)** was a generic assistant prompt with no firm-specific context. It produced functional emails but they were generic — no subject line, no institutional framing, no consistent structure. It could have been written for any industry.

**Revision 1** introduced T. Rowe Price institutional context, a strict two-paragraph structure, a consultative tone, and a fixed sign-off (`All the best, / [Your Name], T. Rowe Price`). Output quality improved meaningfully — emails were on-brand and properly structured — but the subject line appeared inconsistently and the tone occasionally felt stiff and transactional (e.g., "I will promptly send over a case study").

**Revision 2** added an explicit subject line requirement formatted to the client and topic, locked content scope to T. Rowe Price strategies only, and replaced formal tone guidance with natural language instructions (e.g., "write like a trusted colleague"). The result was noticeably more human — the greeting included the client's name, the subject line was specific and intentional, and the body read like something a real person would write rather than a template.

---

## Where the Prototype Still Falls Short

The main risk with this prototype is hallucination. When notes are sparse or ambiguous, the model has a tendency to fill gaps — sometimes fabricating client names, inventing specifics about T. Rowe Price products or capabilities, or making commitments that were never discussed. This is a real problem in an institutional sales context, where accuracy and credibility are critical. Sending an email that references a strategy or number the client never mentioned could damage the relationship.

The model also lacks access to live information about T. Rowe Price's actual product lineup, AUM figures, or fund performance — so any strategy references it generates are based on general training knowledge, not firm data. A rep would need to verify those details before sending.

---

## Deployment Recommendation

This prototype is ready for use as an assisted drafting tool — not as a fully automated send pipeline. The right deployment model is: rep enters notes after a call, app generates a draft, rep reviews and edits before sending. This works particularly well for reps who are traveling between meetings and need a strong starting point quickly. The generated email reliably captures the right structure, tone, and next steps, and typically only needs light personalization before it is ready to send.

Full automation — where emails go out without human review — is not appropriate at this stage. Each institutional client relationship is different, and the rep's judgment about tone, emphasis, and relationship context is still essential. The hallucination risk alone is sufficient reason to keep a human in the loop. But as a baseline generator, the tool already delivers real value.

---

*Prototype built using Google Gemini 2.5 Flash via the `google-genai` Python SDK. Prompts and evaluation cases documented in `prompts.md` and `eval_set.md`.*
