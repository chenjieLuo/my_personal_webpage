from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/curriculum")
def curriculum():
    return render_template('curriculum.html')
@app.route("/education")
def my_education():
    return "<h1>My Education</h1>"
@app.route("/experience")
def my_experience():
    return "<h1>My experience in school and internships</h1>"

#if __name__ == '__main__':
 #   app.run(debug=True)
