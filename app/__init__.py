import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Data
user_data = {"name": "Sam", "about" : "bio", "profilepic": "./static/img/sam.jpg", "github": "link", "linkedin": "link"}


hobbies_data = [
    {"name": "Gym", "image": "static/img/placeholder.png"},
    {"name": "Running", "image": "static/img/placeholder.png"},
    {"name": "Binging KDramas", "image": "static/img/placeholder.png"}
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
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), user=user_data)

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", hobbies=hobbies_data)

@app.route('/education')
def education():
    return render_template('education.html', title="Education", education=education_data)

@app.route('/experiences')
def experiences():
    return render_template('experiences.html', title="Experiences", experiences=experiences_data)

