from openai import OpenAI
import os, json

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def handler(request):
    body = json.loads(request.body)
    pesan = body.get("message")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Kamu adalah chatbot resmi SMK GOLDEN. "
                    "Jurusan: TJKT, Perkantoran, Perhotelan, Pemasaran. "
                    "Jawab singkat, sopan, dan jelas."
                )
            },
            {"role": "user", "content": pesan}
        ]
    )

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "reply": response.choices[0].message.content
        })
  }
