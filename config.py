#Credit Miguel Grinberg
import os
basedir = os.path.abspath(os.path.dirname(__file__))

USER = ""
PASSWORD = ""
DATABASE = ""
CONNECTION_NAME = ""

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = (
            'mysql+pymysql://{user}:{password}@localhost/{database}'
            '?unix_socket=/cloudsql/{connection_name}').format(
                user=USER, password=PASSWORD,
                database=DATABASE, connection_name=CONNECTION_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False