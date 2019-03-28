import os
from main import create_flask_app


environment = os.getenv("FLASK_ENV")
app = create_flask_app(environment)

if __name__ == '__main__':
    app.run(port=9000)
