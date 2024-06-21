import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Data

hobbies_data = [
    {"name": "Gym", "image": "static/img/logo.img"},
    {"name": "Running", "image": "static/img/logo.img"},
    {"name": "Binging KDramas", "image": "static/img/logo.img"}
]

education_data = [
    {
        "school": "School Name 1",
        "img": "/static/img/something",
        "degree": "M.S in Computer Science",
        "year": 2025
    },
    {
        "school": "School Name 2",
        "img": "/static/img/something",
        "degree": "B.S in Computer Science",
        "year": 2021
    }
]

experiences_data = [
    {
        "company_name": "XYZ",
        "position": "Software Engineer",
        "dates": "2023 - 2024",
        "location": "US",
        "description": [
            "bullet point 1",
            "bullet point 2",
        ]
    },
    {
        "company_name": "XYZ2",
        "position": "Software Engineer",
        "dates": "2020 - 2021",
        "location": "US",
        "description": [
            "bullet point 1",
            "bullet point 2",
        ]
    },
]

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    title = "Hobbies"
    return render_template('hobbies.html', title=title, hobbies=hobbies_data)

@app.route('/education')
def education():
    title = "Education"
    return render_template('education.html', title=title, education=education_data)

@app.route('/experiences')
def experiences():
    title = "Experiences"
    return render_template('experiences.html', title=title, experiences=experiences_data)
