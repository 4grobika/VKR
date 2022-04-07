from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def showSignUp():
    return render_template('VKR_main.html')
