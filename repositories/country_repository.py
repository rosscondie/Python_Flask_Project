from db.run_sql import run_sql

from models.country import Country
from models.city import City
import repositories.country_repository as country_repository 

def save(country):
    sql = """INSERT INTO countries 
            (country_name, country_continent, country_population, country_language)
            VALUES (%s, %s, %s, %s) RETURNING *"""
    values = [country.country_name, country.country_continent, country.country_population, country.country_language]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

def select_all():
        countries = []

        sql = "SELECT * FROM countries"
        results = run_sql(sql)

        for row in results:
                country = Country(row['country_name'], row['country_continent'], row['country_population'], row['country_language'], row['id'])
                countries.append(country)
        return countries

def select(id):
        country = None
        sql = "SELECT * FROM countries WHERE id = %s"
        values = [id]
        results = run_sql(sql, values)
        if results:
                result = results[0]
                country = Country(result['country_name'], result['country_continent'], result['country_population'], result['country_language'], result['id'])
        return country

def delete_all():
        sql = "DELETE  FROM countries"
        run_sql(sql)

def delete(id):
        sql = "DELETE  FROM countries WHERE id = %s"
        values = [id]
        run_sql(sql,values)

def update(country):
        sql = """UPDATE countries SET (country_name, country_continent, country_population, country_language)
            = (%s, %s, %s, %s) WHERE id = %s """
        values = [country.country_name, country.country_continent, country.country_population, country.country_language, country.id]
        run_sql(sql, values)

def cities(country):
    cities = []

    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['city_name'], country, row['id'])

        cities.append(city)
    return cities 