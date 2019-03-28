import abc
from .utils import refine_query

class AbsStrategy(abc.ABC):
	@abc.abstractmethod
	def search(self, data, **search_key):
		pass


class MovieNameStrategy(AbsStrategy):
	def search(self, data, **search_key):
		search_matches = map(lambda match: data.retrieve_movie_object(match), data.start_with_prefix(search_key['name'].lower()))
		if search_key['genre'] is not None:
			search_matches = filter(
				lambda match: match['genre'].lower().replace(' ', '') == search_key['genre'].lower().replace(' ', ''),
				search_matches
			)

		if search_key['showing_time'] is not None:
			search_matches = filter(
				lambda match: match['showing_time'].lower().replace(' ', '') == search_key['showing_time'].lower().replace(' ', ''),
				search_matches
			)

		result = list(search_matches)
		return result



class GenreStrategy(AbsStrategy):
	def search(self, data, **search_key):
		refine_genre = refine_query(search_key['genre'])
		result = data.get(refine_genre, [])

		if search_key['showing_time'] is not None and result:
			search_matches = filter(
				lambda match: match['showing_time'].lower().replace(' ', '') == search_key['showing_time'].lower().replace(' ', ''),
				result
			)
			result = list(search_matches)
		return result


class ShowingTimeStrategy(AbsStrategy):
	def search(self, data, **search_key):
		refined_showing_time = refine_query(search_key['showing_time'])
		result = data.get(refined_showing_time, None)
		return result


class SearchMovie(object):
	def __init__(self, strategy):
		self.strategy = strategy

	def objectify(self, search_obj):
		if not search_obj:
			search_obj = []
		else:
			search_obj = search_obj if len(search_obj) > 1 else search_obj[0]
		return search_obj

	def search_movie(self, data, **search_key):
		result = self.strategy.search(data, **search_key)
		return self.objectify(result)
