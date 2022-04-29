from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
