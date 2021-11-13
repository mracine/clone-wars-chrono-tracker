from flask import (
  Blueprint,
  jsonify,
  make_response,
  render_template, 
  request,
)
from flask_cors import CORS, cross_origin
from werkzeug.local import LocalProxy

from .db import get_db


db = LocalProxy(get_db)

bp = Blueprint('tracker', __name__, url_prefix='/api')

CORS(bp)


@bp.route('/', methods=['GET', 'POST', 'OPTIONS'])
def get_episodes():
  """
  Main view for episode tracking status.
  """
  if request.method == 'POST':
    json_data = request.json
    episode_id = json_data.get('episode_id')
    viewed = json_data.get('viewed')

    cur = db.execute(
      'UPDATE episode SET viewed = ? WHERE episode_id = ?',
      (1 if viewed else 0, episode_id)
    )
    db.commit()
    cur.close()

    return 'OK'

  cur = db.execute('SELECT * from episode;');
  data = cur.fetchall()
  cur.close()

  episodes = []
  for i, ep in enumerate(data):
    new_ep = {
      'id': data[i][0],
      'episode_id': data[i][1],
      'name': data[i][2],
      'viewed': data[i][3] != 0,
    }
    episodes.append(new_ep)

  return jsonify(episodes)

