import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country = Country("Germany", "Europe", 832000000, "German")

    def test_country_has_name(self):
        self.assertEqual("Germany", self.country.name)

    def test_country_has_continent(self):
        self.assertEqual("Europe", self.country.continent)

    def test_country_has_population(self):
        self.assertEqual(832000000, self.country.population)

    def test_country_has_language(self):
        self.assertEqual("German", self.country.language)

    # def test_population_returns_as_float(self):
    #     self.assertEqual(83.2, self.country.get_population)