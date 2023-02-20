from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)

# CRUD - CREATE, READ, UPDATE, DELETE 
# RESTful routes - GET, POST, PUT, DELETE

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)

# NEW
# GET "/countries/new"
@countries_blueprint.route("/countries/new")
def new_country():
    return render_template("/countries/new.html")

# SHOW 
# GET "/countries/<id>"
@countries_blueprint.route("/countries/<id>")
def show_country(id):
    country = country_repository.select(id)
    return render_template("/countries/show.html", country = country)