import json

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




