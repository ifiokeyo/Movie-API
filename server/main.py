from os.path import split, abspath
from flask import Flask, jsonify
from flask_restful import Api
from dotenv import load_dotenv


dotenv_path = split(abspath(__file__))[0].replace('server', '.env')
load_dotenv(dotenv_path)

try:
	from api.movies import MovieResource, MovieListResource
except ModuleNotFoundError:
	from server.api.movies import MovieResource, MovieListResource



def create_flask_app(environment):
	# initialize Flask
	app = Flask(__name__, instance_relative_config=True, static_folder=None)
	app.url_map.strict_slashes = False

	# test route
	@app.route('/')
	def index():
		return "Welcome to Maintenance Tracker"


	# create endpoints
	api = Api(app, prefix='/api/v1')

	api.add_resource(
		MovieListResource,
		'/movies',
		endpoint='movies')

	api.add_resource(
		MovieResource,
		'/movies/<int:id>/',
		endpoint="single_movie"
	)


	# handle default 500 exceptions with a custom response
	@app.errorhandler(500)
	def internal_server_error(error):
		response = jsonify(dict(status=500, error='Internal server error',
								message="It is not you. It is me. The server "
								"encountered an internal error and was unable "
								"to complete your request.  Either the server "
								"is overloaded or there is an error in the "
								"application"))
		response.status_code = 500
		return response

	return app

