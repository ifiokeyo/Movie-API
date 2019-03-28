import os
from flask_restful import Resource
from flask import request
from flask import jsonify
from utils.utils import json_reader, get_movie_by_index, build_movie_hash_table
from utils.trie import Trie
from utils.search import MovieNameStrategy, GenreStrategy, ShowingTimeStrategy, SearchMovie

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

json_path = f'{parent_dir}/mockData/movies.json'
movies = json_reader(json_path)


trie = Trie()

Trie.build_movie_trie(trie, movies)

movie_hash_table = build_movie_hash_table(movies)



class MovieListResource(Resource):

	def get(self):
		genre = request.args.get('genre')
		name = request.args.get('name')
		showing_time = request.args.get('showing_time')

		data_obj = {
			'name': name,
			'genre': genre,
			'showing_time': showing_time
		}

		if name is None and genre is None and showing_time is None:
			result = movies

		if name is not None:
			movie_name_strategy = MovieNameStrategy()
			search_handler = SearchMovie(movie_name_strategy)
			result = search_handler.search_movie(trie, **data_obj)

		if name is None and genre is not None:
			movie_genre_strategy = GenreStrategy()
			search_handler = SearchMovie(movie_genre_strategy)
			result = search_handler.search_movie(movie_hash_table, **data_obj)

		if name is None and genre is None and showing_time is not None:
			showing_time_strategy = ShowingTimeStrategy()
			search_handler = SearchMovie(showing_time_strategy)
			result = search_handler.search_movie( movie_hash_table, **data_obj)

		response = jsonify(dict(
			status='success',
			movies=result
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






