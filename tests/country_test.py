import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country = Country("Germany", "Europe", 83200000, "German")

    def test_country_has_name(self):
        self.assertEqual("Germany", self.country.name)
        