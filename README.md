Movie-API
========================

An API for the movie data with custom search implementations.


Development setup
-----------------

- Clone this repo and navigate into the project's directory

  ```console

     $ git clone https://github.com/ifiokeyo/Movie-API && cd movieapi
  ```

- Create a ``python3`` virtual environment for the project and activate it.

  - To install ``python3`` on OSX you can
    follow this ``http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/``

  - Install the virtual environment wrapper ``mkvirtualenv``.

  ```console

     $ mkvirtualenv --py=python3 movieapi
  ```

- Install the project's requirements

  ```console

     $ pip install -r requirements.txt
  ```

- Copy ``.env_sample`` into ``.env`` which is inside the base folder of the project.
  You should adjust it according to your own local settings.


- Run the app: Inside the root directory

  ```console

     $ python server/manage.py
  ```

  - The app should now be available from your browser at ``http://127.0.0.1:9000``

- Run tests:

  ```console
  
     $ cd server/test

     $ python -m unittest
  ```

- Endpoints:

  - To get all movies ``GET http://127.0.0.1:9000/api/v1/movies``.

  - To get a movie using its `id` ``GET http://127.0.0.1:9000/api/v1/movies/<movie_id>``.

  - To search using movie `name` only : ``GET http://127.0.0.1:9000/api/v1/movies?name=<movie_name>``.

  - To search using movie `name` and `genre` only : ``GET http://127.0.0.1:9000/api/v1/movies?name=<movie_name>&genre=<genre>``.

  - To search using movie `name`, `showing_time`, and `genre` :  ``GET http://127.0.0.1:9000/api/v1/movies?name=<movie_name>&genre=<genre>&showing_time=<showing_time>``.

  - To search using movie `showing_time`, and `genre` :  ``GET http://127.0.0.1:9000/api/v1/movies?genre=<genre>&showing_time=<showing_time>``.

  - To search using movie `showing_time` only:  ``GET http://127.0.0.1:9000/api/v1/movies?showing_time=<showing_time>``.

   - To search using movie `genre` only :  ``GET http://127.0.0.1:9000/api/v1/movies?genre=<genre>``.



- To send the API requests on Postman, you can click `follow this <https://www.getpostman.com/docs/postman/sending_api_requests/requests>`_.
