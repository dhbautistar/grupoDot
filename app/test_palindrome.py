from fastapi.testclient import TestClient
from .routes.palindromo import get_palindrome

from main import app

client = TestClient(app)

def test_read_main():
    string = "My dad is a racecar athlete"
    response=get_palindrome(string)
    assert response == "a racecar a"
