from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/curriculum")
def curriculum():
<<<<<<< HEAD
    return render_template('curriculum.html')

if __name__ == '__main__':
	app.run(debug=True)
=======
    return "<h1>The curriculums I have taken</h1> "
@app.route("/education")
def my_education():
    return "<h1>My Education</h1>"
@app.route("/experience")
def my_experience():
    return "<h1>My experience in school and internships</h1>"
>>>>>>> f1478b5cf71d7c8f54c056ea372bad4a0a1854ec
