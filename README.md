Movie-API
========================

An API for the movie data with custom search implementations.


Development setup
-----------------

- Clone this repo and navigate into the project's directory

  .. code-block:: 
  
  console

     $ git clone https://github.com/ifiokeyo/Movie-API && cd movieapi

- Create a ``python3`` virtual environment for the project and activate it.

  - To install ``python3`` on OSX you can
    `follow this <http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/>`_

  - To install the virtual environment wrapper ``mkvirtualenv`` you can
    `follow this <https://jamie.curle.io/installing-pip-virtualenv-and-virtualenvwrapper-on-os-x>`_.

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

- Run tests:
  
  ```console
  
     $ cd server/test

     $ python -m unittest
  ```


- The app should now be available from your browser at ``http://127.0.0.1:9000``

- To send the API requests on Postman, you can click `follow this <https://www.getpostman.com/docs/postman/sending_api_requests/requests>`_.

