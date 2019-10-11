import os
import pandas as pd
import numpy as np
import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


uid = "spookybootcamp@spookybootcamp"
pwd = "$pooky123"
database = "spooky"
server = "spookybootcamp.postgres.database.azure.com"

engine = create_engine(f"postgres://{uid}:{pwd}@{server}/{database}")

inspector = inspect(engine)
spooky = inspector.get_table_names()

print("Tables are -->", spooky)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

###################################################################

@app.route("/inspiration/")
def costumes():

    conn = engine.connect()
    data_inspiration = pd.read_sql("select * from costumes_inspiration", conn)
    data_expenditure = pd.read_sql("select * from costumes_expenditure", conn)
    data_pets = pd.read_sql("select * from costumes_pets", conn)
    data_theme = pd.read_sql("select * from costumes_themes", conn)
    data_state = pd.read_sql("select * from costumes_by_state", conn)


    # Create a dictionary from the row data and append to a list of sources of inspiration
    costumes = {
        "Source of inspiration": data_inspiration["source of inspiration"].tolist(),
        "Men": data_inspiration.men.values.tolist(),
        "Women": data_inspiration.women.values.tolist(),
        "Year": data_expenditure.year.values.tolist(),
        "Adult": data_expenditure.adult.values.tolist(),
        "Children": data_expenditure.children.values.tolist(),
        "Pet": data_expenditure.pet.values.tolist(),
        "Costume_Pets": data_pets.costume.tolist(),
        "Pets_Percent": data_pets.percentage.values.tolist(),
        "Theme": data_theme.theme.tolist(),
        "Theme_Percent": data_theme.percentage.values.tolist(),
        "State": data_state.State.tolist(),
        "Most_Popular_Costume": data_state["Most Popular Costume"].tolist()

    }

    print(costumes)

    return jsonify(costumes)

@app.route("/costumes.html")
def costume_page():
    """Return costumes page."""
    return render_template("costumes_page.html")


@app.route("/movies")
def movies():
    conn = engine.connect()
    data_movies = pd.read_sql('select * , "No. of Reviews" / 4 as radius from movies', conn)

    movies = {
        "Rank": data_movies.Rank.values.tolist(),
        "Tomato_Meter": data_movies.RatingTomatometer.values.tolist(),
        "Title": data_movies.Title.tolist(),
        "Number_Reviews": data_movies['No. of Reviews'].values.tolist(), 
        "radius": data_movies['radius'].values.tolist()
    }

    return jsonify(movies)

@app.route("/movie.html")
def movies_render():
    """Return movies page."""
    return render_template("movie.html")


@app.route("/candy.html")
def candies():
    return render_template("candy.html")


@app.route("/haunted/")
def haunted():
    conn = engine.connect()
    haunted_city = pd.read_sql("select * from haunted_places_city", conn)
    haunted_state = pd.read_sql("select * from haunted_places_state", conn)
    
    dataHaunted = {
        "city_city": haunted_city.City.tolist(),
        "city_state": haunted_city.State.tolist(),
        "city_qnty": haunted_city.Quantity.values.tolist(),
        "state_state": haunted_state.State.tolist(),
        "state_quantity": haunted_state.Quantity.values.tolist()
    }
    
    print(dataHaunted)
    
    return jsonify(dataHaunted)


@app.route("/haunted-places.html")
def places():
    """Return haunted-places page."""
    
    return render_template("haunted-places.html")
    
    
if __name__ == "__main__":
    app.run()