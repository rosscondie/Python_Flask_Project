import pdb
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

# country_repository.delete_all()
# city_repository.delete_all()

city1 = City("Hannover", "Germany")
city_repository.save(city1)
city2 = City("Edinburgh", "Scotland")
city_repository.save(city2)

country1 = Country("Germany", "Europe", 832000000, "German", city1)
country_repository.save(country1)
country2 = Country("Scotland", "Europe", 5000000, "English", city2)
country_repository.save(country2)