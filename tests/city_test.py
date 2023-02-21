import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City("Hannover", "Germany")

    def test_city_has_name(self):
        self.assertEqual("Hannover", self.city.city_name)

    def test_city_has_country(self):
        self.assertEqual("Germany", self.city.country)

    def test_city_has_no_id_initially(self):
        self.assertIsNone(self.city.id)

    

