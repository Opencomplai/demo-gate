"""Rank incoming job applications by fit for the role."""
from openai import OpenAI

client = OpenAI()


def score_cv(cv_text: str, role: str) -> float:
    reply = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"Score this CV from 0 to 1 for the role: {role}. Reply with the number only."},
            {"role": "user", "content": cv_text},
        ],
    )
    return float(reply.choices[0].message.content)
