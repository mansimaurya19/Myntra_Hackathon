import sqlite3
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from idiot import search
# from asr_myntra import speech_text


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)


@app.route('/')
def index():
 return render_template("home.html")



@app.route('/voice',methods=['POST'])
def voice():
    query = request.form['voice_query']
   # print(query)
   # path = speech_text(query)
   # print(path)
    return render_template("home.html")
   




    

@app.route('/region/<string:region>',methods=['GET'])
def north(region):
    df = search(region)
    print(df)
    return render_template("results.html",data=df)


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
