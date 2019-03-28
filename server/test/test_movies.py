import unittest
import json, os, sys
from base import BaseTestCase

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class MovieTestCase(BaseTestCase):

	def test_fetch_all_movies_successfully(self):
		response = self.client.get('/api/v1/movies', content_type="application/json")
		response_data = json.loads(response.data)

		self.assertEqual(len(response_data['movies']), 1000)
		self.assert_status(response, 200)

	def test_fetch__movie_by_id_successfully(self):
		response = self.client.get('/api/v1/movies/900', content_type="application/json")
		response_data = json.loads(response.data)

		self.assertEqual(response_data['movie']['id'], 900)
		self.assert_status(response, 200)

	def test_fail__fetch_movie_by_id(self):
		response = self.client.get('/api/v1/movies/10000', content_type="application/json")
		response_data = json.loads(response.data)

		self.assertEqual(response_data['status'], 'fail')
		self.assert_status(response, 404)

	def test_search_movies_by_movie_name(self):
		response = self.client.get('/api/v1/movies?name=Clouds of Sils Maria', content_type="application/json")
		response_data = json.loads(response.data)

		self.assertEqual(response_data['movies']['name'], 'Clouds of Sils Maria')
		self.assert_status(response, 200)

	def test_search_movies_by_movie_name_and_genre(self):
		response = self.client.get('/api/v1/movies?name=Tai Chi Hero&genre=Action|Comedy|Drama|Fantasy|Sci-Fi|IMAX', content_type="application/json")
		response_data = json.loads(response.data)

		self.assertEqual(response_data['movies']['name'], 'Tai Chi Hero')
		self.assert_status(response, 200)

	def test_search_movies_by_partial_movie_name_and_genre(self):
		response = self.client.get('/api/v1/movies?name=The&genre=Drama', content_type="application/json")
		response_data = json.loads(response.data)

		self.assertGreater(len(response_data['movies']), 1)
		self.assert_status(response, 200)


if __name__ == '__main__':
	unittest.main()
