import os

from flask import Flask
from flask_cors import CORS


def create_app(test_config=None):
  """
  Creates and configures the Flask app.
  """
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'clonewars.db')
  )

  if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
  else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

  # TODO: any other app config
  # TVDB_SERIES_ID = 83268

  try:
    os.makedirs(app.instance_path)
  except OSError:
    # TODO: log here
    pass
  
  from .db import init_app
  init_app(app)

  from . import tracker
  app.register_blueprint(tracker.bp)

  CORS(app)

  return app
