from db.run_sql import run_sql

from models.city import City
from models.country import Country

def save(city):
    sql = "INSERT INTO cities (city_name, country) VALUES (%s, %s) RETURNING *"
    values = [city.city_name, city.country]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def select_all():
    cities = []
    
    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        city = City(row['city_name'], row['country'], row['id'])
        cities.append(city)
        return cities

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        city = City(result['city_name'], result['country'], result['id'])
    return city 

def delete_all():
    sql = "DELETE  FROM cities"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(city):
    sql = "UPDATE cities SET (city_name, country) = (%s, %s) WHERE id = %s"
    values = [city.city_name, city.country, city.id]
    run_sql(sql, values)

def countries(city):
    countries = []

    sql = "SELECT * FROM countries WHERE city_id = %s"
    values = [city.id]
    results = run_sql(sql, values)

    for row in results:
        # Should I add city here?
        country = Country(row['country_name'], row['country_continent'], row['country_population'], row['country_language'], row['id'])
        countries.append(country)
    return countries 