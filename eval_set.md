# Evaluation Set

Five test cases for evaluating the sales follow-up email generator.

---

## Case 1 — Normal

**Label:** Normal / Structured Notes

**Raw Input Notes:**
```
Met with Sarah Chen, VP of Operations at Meridian Logistics.
30-min intro call. She's evaluating tools to reduce manual reporting time for her team of 12.
Current stack: Excel, some Salesforce. Pain point: weekly report takes ~4 hours to compile.
Interested in our dashboard integration. Wants to see a demo with their actual data.
Budget not confirmed yet — she needs to loop in her director.
Follow-up: send case study from similar logistics client, schedule demo for week of April 21.
```

**What a good output should do:**
- Open with a warm but professional thank-you for Sarah's time
- Briefly recap the core pain point (manual reporting) and the relevant solution discussed
- Confirm the two agreed-upon next steps: sending the case study and scheduling a demo
- Acknowledge that budget alignment is pending without applying pressure
- Avoid filler phrases like "It was an absolute pleasure!" or excessive exclamation points
- Close with a clear, low-friction call to action

---

## Case 2 — Normal

**Label:** Normal / Action-Heavy Call

**Raw Input Notes:**
```
Call with Marcus Reed, Director of Sales at Brightfield Media. 45 mins.
They've been using a competitor — contract up in 60 days. Actively looking to switch.
Key concerns: onboarding speed and API reliability. We addressed both.
He liked the pricing tier we proposed. Wants contract draft sent by EOW.
Also asked about SSO support — confirmed it's on our roadmap for Q3.
Next steps: send contract draft, intro him to our solutions engineer (Jamie), confirm onboarding timeline.
```

**What a good output should do:**
- Thank Marcus and reference the context of the conversation (evaluation ahead of contract renewal)
- Summarize the key concerns raised (onboarding, API reliability) and briefly affirm they were addressed
- Clearly list the committed next steps: contract draft by end of week, intro to Jamie, onboarding timeline
- Note the SSO roadmap item accurately without overpromising a delivery date
- Maintain a confident, forward-moving tone appropriate for a near-close deal

---

## Case 3 — Edge

**Label:** Edge / Sparse Notes

**Raw Input Notes:**
```
talked to someone at acme. seemed interested. might follow up.
```

**What a good output should do:**
- Produce a minimal, generic follow-up that does not invent names, roles, topics, or next steps
- Thank the contact for their time without fabricating specifics about what was discussed
- Express openness to continuing the conversation and invite them to reach out
- Avoid placeholder text like "[insert topic here]" — the email should be usable as-is
- Not speculate on interest level or timeline beyond what the notes support

---

## Case 4 — Hallucination-Risk

**Label:** Hallucination-Risk / Ambiguous and Contradictory Notes

**Raw Input Notes:**
```
Met w/ someone from either TechNova or NovaTech — couldn't find the calendar invite.
Discussed pricing — I think we offered 20% off? Or maybe that was a different call.
They mentioned a team of 50 or 500, wasn't sure.
Could be a good fit. Or maybe they're not the right buyer.
Next steps: ??? Follow up maybe in a few weeks or a month.
```

**What a good output should do:**
- Use cautious, non-committal language throughout (e.g., "following up on our recent conversation" rather than asserting specifics)
- Avoid stating any figures, discounts, or company details that are unconfirmed
- Not fabricate a company name, team size, or pricing offer
- Optionally include a soft internal flag or note suggesting the sender verify details before sending
- Keep the email brief and open-ended, leaving room for the prospect to re-establish context if needed

---

## Case 5 — Edge (Multilingual / Non-Native Speaker Notes)

**Label:** Edge / Fragmented Notes from Non-Native English Speaker

**Raw Input Notes:**
```
call with roberto from spain office. he say they have problem with the data import not working good.
want to see how we fix. budget ok he say. next step send him video or document how to use.
maybe also schedule again in 2 week.
```

**What a good output should do:**
- Produce a fully polished, grammatically correct professional email regardless of note quality
- Accurately reflect the substance: data import issue, interest in solution documentation, follow-up meeting in ~2 weeks
- Not "correct" or comment on the note style — treat the content as valid input
- Avoid adding details not present (e.g., do not invent a company name or specific product feature)
- Demonstrate that the tool is robust to informal or non-native input without degrading output quality
