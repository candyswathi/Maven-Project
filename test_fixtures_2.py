import pytest

#  Define a fixture that returns a dictionary
@pytest.fixture
def sample_data():
    return {
        "name": "John",
        "age": 25,
        "city": "New York"
    }

#  Test function using the fixture
def test_name(sample_data):
    assert sample_data["name"] == "John"

def test_age(sample_data):
    assert sample_data["age"] == 25

def test_city(sample_data):
    assert sample_data["city"] == "New York"

#  Additional test with modified fixture data
@pytest.fixture
def updated_data():
    return {
        "name": "Alice",
        "age": 30,
        "city": "Los Angeles"
    }

def test_updated_name(updated_data):
    assert updated_data["name"] == "Alice"

def test_updated_age(updated_data):
    assert updated_data["age"] == 30

def test_updated_city(updated_data):
    assert updated_data["city"] == "Los Angeles"
