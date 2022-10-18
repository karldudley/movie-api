''' movies controller '''
from werkzeug.exceptions import BadRequest
import app

def index(req):
    movie = app.query_db('select * from movie;')
    return movie, 200

def show(req, uid):
  fetch_result = find_by_uid(uid)
  if fetch_result == []:
    raise BadRequest(f"We don't have a movie with that ID of {uid}")
  else:
    return fetch_result, 200

def create(req):
  new_movie = req.get_json()
  return_value = app.query_db('insert into movie (title, rating, genre) values (?, ?, ?);', (new_movie["title"], new_movie["rating"], new_movie["genre"]))
  check_value = app.query_db('select id from movie where title = (?);', (new_movie["title"],))
  return check_value, 201

# def update(req, uid):

# def destroy(req, uid):


def find_by_uid(uid):
  try:
    return app.query_db('select * from movie where id = (?);', (uid,))
  except:
    raise BadRequest(f"We don't have a movie with that ID of {uid}")
