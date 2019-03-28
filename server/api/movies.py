import os
from flask_restful import Resource
from flask import request
from flask import jsonify
from utils.utils import json_reader, get_movie_by_index
from utils.trie import Trie

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

json_path = f'{parent_dir}/mockData/movies.json'
movies = json_reader(json_path)


trie = Trie()

Trie.build_movie_trie(trie, movies)



class MovieListResource(Resource):

	def get(self):
		genre = request.args.get('genre')
		name = request.args.get('name')
		showing_time = request.args.get('showing_time')

		if name is not None:
			search_matches = map(lambda match: trie.retrieve_movie_object(match), trie.start_with_prefix(name.lower()))

			if genre:
				search_matches = filter(
					lambda match: match['genre'].lower().replace(' ', '') == genre.lower().replace(' ', ''),
					search_matches
				)

			if showing_time:
				search_matches = filter(
					lambda match: match['showing_time'].lower().replace(' ', '') == showing_time.lower().replace(' ', ''),
					search_matches
				)

			result = list(search_matches)


			if not result:
				result = []

			result = result if len(result) > 1 else result[0]

			response = jsonify(dict(
				status='success',
				movies=result
			))
		else:
			response = jsonify(dict(
				status='success',
				movies=movies
			))

		response.status_code = 200
		return response

class MovieResource(Resource):
	def get(self, id):
		result = get_movie_by_index(movies, id)

		if result is None:
			response = jsonify(dict(
				status='fail',
				message='Movie not found'
			))
			response.status_code = 404

		else:
			response = jsonify(dict(
				status='success',
				movie=result
			))
			response.status_code = 200
		return response






