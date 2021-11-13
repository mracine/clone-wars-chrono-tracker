import click, sqlite3
from flask import current_app, g
from flask.cli import with_appcontext

from .csv_importer import parse_csv

DATABASE = 'clonewars.db'

def init_app(app):
  """
  Adds cli utilities and sets up app with db capability.
  """
  app.cli.add_command(init_db_command)
  app.teardown_appcontext(close_connection)


@click.command('init-db')
@with_appcontext
def init_db_command():
  """
  cli utility to clear and recreate the database.
  """
  init_db()
  click.echo('Initialized the database.')

  # TODO: change path
  episodes = parse_csv(
    '/home/mrracine/projects/clone-wars-server/clonewars.csv',
    has_header=True
  )

  db = get_db()
  db_rows = []
  for ep in episodes:
    db_rows.append((ep.id, ep.name, ep.viewed))

  db.executemany(
    'INSERT INTO episode (episode_id, name, viewed) VALUES (?, ?, ?)',
    db_rows
  )
  db.commit()

  click.echo('Loaded database.')


def get_db():
  """
  Returns the db if it exists. Else, creates it.
  """
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = sqlite3.connect(
      current_app.config.get('DATABASE')
    )

  return db


def init_db():
  """
  Initializes the database.
  """
  db = get_db()

  with current_app.open_resource('schema.sql') as f:
    db.executescript(f.read().decode('utf8'))


def close_connection(exception):
  """
  Closes the connection to the database.
  """
  if exception:
    print(exception)

  db = getattr(g, '_database', None)
  if db is not None:
    db.close()

