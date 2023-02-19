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