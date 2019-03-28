import json, re

def json_reader(file_path):
	with open(file_path, 'r') as file:
		data = file.read()
		movies = json.loads(data)
	return movies


def get_movie_by_index(movies, id):
	low = 0
	high = len(movies) - 1

	while low <= high:
		mid = (low + high) // 2

		if movies[mid]['id'] < id:
			low = mid + 1
		elif movies[mid]['id'] > id:
			high = mid - 1
		else:
			return movies[mid]
	return None


def refine_query(query):
	if re.search('[0-9]\S+\s*(AM|PM)|[0-9]\S+\s*(am|pm)', query):
		query = '{} {}'.format(query[:-2].strip(' '), query[-2:].upper())
	else:
		query = query.capitalize()

	return query


def build_movie_hash_table(movies):
	result = {}
	for movie in movies:
		if movie['genre']:
			if re.search('\W+', movie['genre']):
				genre_str = movie['genre'].split('|')
				for term in genre_str:
					result.setdefault(term, []).append(movie)
			else:
				result.setdefault(movie['genre'], []).append(movie)
		if movie['showing_time']:
			result.setdefault(movie['showing_time'], []).append(movie)

	return result







