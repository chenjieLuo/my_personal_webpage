from flask import Flask, render_template
#from forms import RegistrationForm, LoginForm
app = Flask(__name__)

#app.config['SECRET_KEY'] = 'b581b86194d44e7069a0664a7f4313ee'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/curriculum")
def curriculum():
    return render_template('curriculum.html')
@app.route("/education")
def education():
    return render_template('education.html')
@app.route("/experience")
def experience():
	return render_template('experience.html')
#@app.route("/experience")

#if __name__ == '__main__':
#    app.run(debug=True)
