import pytest
import requests

class TestGames:
    url = 'http://localhost:8000/api/games'

    def test_list_games(self):
        response = requests.get(self.url)
        assert response.status_code == 200


    def test_create_game(self):
        response = requests.post(f"{self.url}/create", {"users":["matisla"], "best_of": 3, "max_score": 501, "mode": "single"})
        assert response.status_code == 200

