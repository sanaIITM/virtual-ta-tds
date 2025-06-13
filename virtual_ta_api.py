from flask import Flask, request, jsonify
import json
import os
from openai import OpenAI

# Load your OpenAI key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load structured course content
with open("tds_structured.json", "r", encoding="utf-8") as f:
    course_data = json.load(f)

app = Flask(__name__)

def find_relevant_content(query):
    matched = []
    for module, topics in course_data.items():
        for title, content in topics.items():
            if query.lower() in title.lower() or query.lower() in content.lower():
                matched.append(f"{module} > {title}:\n{content}")
    return "\n\n".join(matched[:3])  # top 3 matches

@app.route("/ask", methods=["POST"])
def ask_virtual_ta():
    data = request.json
    question = data.get("question", "")
    context = find_relevant_content(question)

    if not context:
        context = "No relevant course content found. Please rephrase your question."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a teaching assistant answering questions using the following course content."},
            {"role": "user", "content": f"Course Content:\n{context}\n\nQuestion: {question}"}
        ]
    )

    answer = response.choices[0].message.content
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)

