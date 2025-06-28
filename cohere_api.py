# cohere_api.py
import cohere

co = cohere.Client('z442CDaQs13dge4XZD5jJxwjwlqOEDcYyLFZtwdt')

def generate_ideas(topic):
    response = co.chat(model='command-nightly', message=f"Generate 5 creative project ideas for: {topic}")
    return response.text

def find_subtopics(topic):
    response = co.chat(model='command-nightly', message=f"List important subtopics related to: {topic}")
    return response.text

def write_pitch(topic):
    response = co.chat(model='command-nightly', message=f"Write an elevator pitch for a project on: {topic}")
    return response.text

def generate_problems(domain):
    response = co.chat(model='command-nightly', message=f"List real-world problems in the domain of: {domain}")
    return response.text

def recommend_projects(domain):
    response = co.chat(model='command-nightly', message=f"Recommend 3 innovative project ideas related to: {domain}")
    return response.text
