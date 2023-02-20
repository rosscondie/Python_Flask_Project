from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities/new")
def new_city():
    return render_template("/cities/new.html")

@cities_blueprint.route("/cities", methods=['POST'])
def create_city():
    city_name = request.form['city_name']
    city = City(city_name)
    city_repository.save(city)
    return redirect("/cities")