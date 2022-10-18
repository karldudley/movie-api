''' movies controller '''
from werkzeug.exceptions import BadRequest
import app

movies = [
    {'id': 1, 'title': 'Shrek 2', 'rating': 5, 'genre': 'epic'},
    {'id': 2, 'title': 'Entergalactic', 'rating': 4, 'genre': 'animated rom-com' },
    {'id': 3, 'title': 'Prisoners', 'rating': 4, 'genre':'thriller'}
]

def index(req):
    # return [c for c in movies], 200
    movie = app.query_db('select * from movie;')
    return movie, 200

def show(req, uid):
    return find_by_uid(uid), 200

def create(req):
    new_cat = req.get_json()
    new_cat['id'] = sorted([c['id'] for c in movies])[-1] + 1
    movies.append(new_cat)
    return new_cat, 201

def update(req, uid):
    cat = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        cat[key] = val
    return cat, 200

def destroy(req, uid):
    cat = find_by_uid(uid)
    movies.remove(cat)
    return cat, 204

def find_by_uid(uid):
    try:
        return next(cat for cat in movies if cat['id'] == uid)
    except:
        raise BadRequest(f"We don't have that cat with id {uid}!")
