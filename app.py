from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from controllers import movies
from werkzeug import exceptions

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db.init_app(app)
CORS(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return self.name

@app.route('/')
def home():
    init_db()
    return jsonify({'message': 'Hello from Flask!'}), 200

@app.route('/api/movies', methods=['GET', 'POST'])
def movies_handler():
    fns = {
        'GET': movies.index,
        'POST': movies.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/api/movies/<int:movie_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def movie_handler(movie_id):
    fns = {
        'GET': movies.show,
        'PATCH': movies.update,
        'PUT': movies.update,
        'DELETE': movies.destroy
    }
    resp, code = fns[request.method](request, movie_id)
    return jsonify(resp), code

def get_db():
  with app.app_context():
    from app import db
    db.create_all()
  return db

def init_db():
  with app.app_context():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)
