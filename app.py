from flask import Flask, request
from flask_cors import CORS
import db

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/movies")
def index():
    return db.movies_all()


@app.route("/movies.json", methods=["POST"])
def create():
    # print(f"Processing Create request: #{request}")
    data = request.get_json()
    title = data.get("title")
    year = data.get("year")
    genre = data.get("genre")
    description = data.get("description")
    image = data.get("image")
    return db.movies_create(title, year, genre, description, image)


@app.route("/movies/<id>.json")
def show(id):
    return db.movies_find_by_id(id)


@app.route("/movies/<id>.json", methods=["PATCH"])
def update(id):
    title = request.form.get("title")
    year = request.form.get("year")
    genre = request.form.get("genre")
    description = request.form.get("description")
    image = request.form.get("image")
    return db.movies_update_by_id(id, title, year, genre, description, image)

