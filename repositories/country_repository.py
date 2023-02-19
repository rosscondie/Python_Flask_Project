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

def select_all():
        countries = []

        sql = "SELECT * FROM countries"
        results = run_sql(sql)

        for row in results:
                city = city_repository.select(row['city_id'])
                country = Country(row['country_name'], row['country_continent'], row['country_population'], row['country_language'], city, row['id'])
                countries.append(country)
        return countries

