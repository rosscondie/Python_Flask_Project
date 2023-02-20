import pdb
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

city_repository.delete_all()
country_repository.delete_all()

country1 = Country("Germany", "Europe", 83200000, "German")
country_repository.save(country1)
country2 = Country("Scotland", "Europe", 5000000, "English")
country_repository.save(country2)

city1 = City("Hannover", country1)
city_repository.save(city1)
city2 = City("Edinburgh", country2)
city_repository.save(city2)

test_get_all_cities = city_repository.select_all()
# test_get_one_city = city_repository.select(9)

city1.city_name = "Berlin"

city_repository.update(city1)
test_updated_cities = city_repository.select_all()

test_country1_cities = country_repository.cities(country1)

breakpoint()