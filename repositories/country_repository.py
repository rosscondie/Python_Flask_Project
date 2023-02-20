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

def select(id):
        country = None
        sql = "SELECT * FROM countries WHERE id = %s"
        values = [id]
        results = run_sql(sql, values)
        if results:
                result = results[0]
                city = city_repository.select(result['city_id'])
                country = Country(result['country_name'], result['country_continent'], result['country_population'], result['country_language'], city, result['id'])
        return country

def delete_all():
        sql = "DELETE  FROM countries"
        run_sql(sql)

def delete(id):
        sql = "DELETE  FROM countries WHERE id = %s"
        values = [id]
        run_sql(sql,values)

def update(country):
        sql = """UPDATE countries SET (country_name, country_continent, country_population, country_language, city_id)
            = (%s, %s, %s, %s, %s) WHERE id = %s """
        values = [country.country_name, country.country_continent, country.country_population, country.country_language, country.city.id, country.id]
        run_sql(sql, values)