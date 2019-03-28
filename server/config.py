from os.path import abspath, split, dirname

from dotenv import load_dotenv


dotenv_path = split(abspath(__file__))[0].replace('server', '.env')
load_dotenv(dotenv_path)


class Config(object):
    BASE_DIR = dirname(__file__)
    debug = True

class TestingConfiguration(Config):
    TESTING = True
    DEBUG = False
    JSONIFY_PRETTYPRINT_REGULAR=False

app_configuration = {
    'development': Config,
    'testing': TestingConfiguration
}