from flask import Flask
app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"
@app.route("/curriculum")
def curriculum():
    return "<h1>The curriculums I have taken</h1> "
