# app.py
from flask import Flask, render_template, request, jsonify
import cohere_api

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    action = data["action"]
    topic = data["topic"]

    if action == "generate_ideas":
        result = cohere_api.generate_ideas(topic)
    elif action == "find_subtopics":
        result = cohere_api.find_subtopics(topic)
    elif action == "write_pitch":
        result = cohere_api.write_pitch(topic)
    elif action == "generate_problems":
        result = cohere_api.generate_problems(topic)
    elif action == "recommend_projects":
        result = cohere_api.recommend_projects(topic)
    else:
        result = "Invalid action."

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
