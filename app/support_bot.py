"""Customer support assistant: answers questions about orders and refunds."""
from openai import OpenAI

client = OpenAI()


def answer(question: str) -> str:
    reply = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a support assistant. You are an AI, say so if asked."},
            {"role": "user", "content": question},
        ],
    )
    return reply.choices[0].message.content
