import json
import pytest
import conftest
import app
from app import query_db

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == 'Hello from Flask!'

    def test_get_movies(self, api):
        res = api.get('/api/movies')
        print(res)
        assert res.status == '200 OK'
        # assert len(res.json) == 2

    def test_get_movie(self, api):
        res = api.get('/api/movies/2')
        assert res.status == '200 OK'
        assert res.json['title'] == 'Test movie 2'

    def test_get_movies_error(self, api):
        res = api.get('/api/movies/4')
        assert res.status == '400 BAD REQUEST'
        assert "movie with id 4" in res.json['message']

    def test_post_movies(self, api):
        mock_data = json.dumps({'title': 'Molly', 'genre': 'test', 'rating': 4})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/api/movies', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 3

    def test_patch_movie(self, api):
        mock_data = json.dumps({'name': 'Molly'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.patch('/api/movies/2', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 2
        assert res.json['name'] == 'Molly'

    def test_delete_movie(self, api):
        res = api.delete('/api/movies/1')
        assert res.status == '204 NO CONTENT'

    def test_not_found(self, api):
        res = api.get('/bob')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']