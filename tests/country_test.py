import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country = Country("Germany", "Europe", 83200000, "German")

    def test_country_has_name(self):
        self.assertEqual("Germany", self.country.country_name)

    def test_country_has_continent(self):
        self.assertEqual("Europe", self.country.country_continent)

    def test_country_has_population(self):
        self.assertEqual(83200000, self.country.country_population)

    def test_country_has_language(self):
        self.assertEqual("German", self.country.country_language)

    def test_country_has_no_id_initially(self):
        self.assertIsNone(self.country.id)

    def test_country_has_an_id(self):
        country = Country("Scotland", "Europe", 5000000, "English/Gaelic", 9)
        self.assertIsNotNone(country.id)

    def test_population_returns_as_formatted_string(self):
        self.assertEqual("83.2 Million" , self.country.get_population())