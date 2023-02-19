from db.run_sql import run_sql

from models.country import Country
from models.city import City
import repositories.city_repository as city_repository 

def save(country):
    sql = """INSERT INTO countries 
            (country_name, country_continent, country_population, country_language, city_id)
            VALUES (%s, %s, %s, %s, %s) RETURNING *"""
    values = [country.country_name, country.country_continent, country.country_population, country.country_language, country.city.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country