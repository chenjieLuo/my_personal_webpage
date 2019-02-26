from flask import Flask
app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"
@app.route("/curriculum")
def curriculum():
    return "<h1>The curriculums I have taken</h1> "
@app.route("/education")
def my_education():
    return "<h1>My Education</h1>"
@app.route("/experience")
def my_experience():
    return "<h1>My experience in school and internships</h1>"
