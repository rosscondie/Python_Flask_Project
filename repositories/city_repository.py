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