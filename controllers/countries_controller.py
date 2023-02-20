from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
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

# CREATE
# POST "/countries"
@countries_blueprint.route("/countries", methods=['POST'])
def create_country():
    country_name = request.form['country_name']
    country_continent = request.form['country_continent']
    country_population = request.form['country_population']
    country_language = request.form['country_language']
    country = Country(country_name, country_continent, country_population, country_language)
    country_repository.save(country)
    return redirect("/countries")

# SHOW 
# GET "/countries/<id>"
@countries_blueprint.route("/countries/<id>")
def show_country(id):
    country = country_repository.select(id)
    return render_template("/countries/show.html", country = country)

# EDIT
# GET "/countries/<id>/edit"
@countries_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    country = country_repository.select(id)
    return render_template("/countries/edit.html", country = country)