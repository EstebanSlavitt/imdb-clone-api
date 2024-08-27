from flask import Flask, request
import db

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/movies")
def index():
    return db.movies_all()

@app.route("/movies.json", methods=["POST"])
def create():
    title = request.form.get("title")
    year = request.form.get("year")
    genre = request.form.get("genre")
    description = request.form.get("description")
    image = request.form.get("image")
    return db.movies_create(title, year, genre, description, image)
