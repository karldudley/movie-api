import pytest
import app
import controllers.movies

print(dir(controllers.movies))

@pytest.fixture
def api(monkeypatch):
    mock_movies = [
        {'id': 1, 'title': 'Test Movie 1', 'rating': 7, 'genre': 'test'},
        {'id': 2, 'title': 'Test Movie 2', 'rating': 4, 'genre': 'test'}
    ]
    monkeypatch.setattr(controllers.movies, "app", mock_movies)
    api = app.app.test_client()
    return api