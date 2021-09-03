import unittest
from city_functions import city_string

class TestCityCountry(unittest.TestCase):

	def test_city_country(self):
		formatted_city_name = city_string('Pretoria', 'South Africa')
		self.assertEqual(formatted_city_name, 'Pretoria, South Africa')

	def test_city_country_population(self):
		formatted_city_with_population = city_string('Harare', 'Zimbabwe', 'population = 5_000_000')

if __name__ == '__main__':
	unittest.main()