import pytest
from validator.Validator import Validator


@pytest.fixture
def schema():
    v = Validator()
    schema = v.dict()
    return schema


def test_dictvalidator(schema):
    v = Validator()
    schema.shape({
        'name': v.string().required(),
        'age': v.number().positive(),
        })
    assert schema.is_valid({'name': 'kolya', 'age': 100})
    assert schema.is_valid({'name': 'maya', 'age': None})
    assert not schema.is_valid({'name': '', 'age': None})
    assert not schema.is_valid({'name': 'ada', 'age': -5})


def test_dictvalidator_2(schema):
    v = Validator()
    schema.shape({
        "Greet": v.string().min_len(6).contains('Hello'),
        "Friends": v.list().sizeof(2),
        "Age": v.number().positive().range(14, 120)
        })

    assert schema.is_valid({
        "Greet": "Hello Bob!",
        "Friends": ["Dima", "Lesha"],
        "Age": 42})
    assert schema.is_valid({
        "Greet": None,
        "Friends": ["Dima", "Lesha"],
        "Age": 42})
    assert not schema.is_valid({
        "Greet": "Goodby",
        "Friends": ["Bob"],
        "Age": -8})
    assert not schema.is_valid({
        "Greet": "Hello Maks!",
        "Friends": ["Sahsa", "Ron"],
        "Age": 8})
    assert not schema.is_valid({
        "Greet": "Hello Gerda",
        "Friends": [],
        "Age": 35})
    assert not schema.is_valid({
        "Greet": "Hello",
        "Friends": ["Vity", "Grisha"],
        "Age": 35})
    assert schema.is_valid({"Greet": None, "Friends": None, "Age": None})


def test_dictvalidator_3(schema):
    v = Validator()
    schema.shape({
        "Greet": v.string().required().min_len(6).contains('Hello'),
        "Friends": v.list().required().sizeof(2),
        "Age": v.number().required().positive().range(14, 120)
        })
    assert schema.is_valid({
        "Greet": "Hello Bob!",
        "Friends": ["Dima", "Lesha"],
        "Age": 42})
    assert not schema.is_valid({
        "Greet": None,
        "Friends": ["Dima", "Lesha"],
        "Age": 42})
    assert not schema.is_valid({
        "Greet": "Goodby",
        "Friends": ["Bob"],
        "Age": -8})
    assert not schema.is_valid({
        "Greet": "Hello Maks!",
        "Friends": ["Sahsa", "Ron"],
        "Age": 8})
    assert not schema.is_valid({
        "Greet": "Hello Gerda",
        "Friends": [],
        "Age": 35})
    assert not schema.is_valid({
        "Greet": "Hello",
        "Friends": ["Vity", "Grisha"],
        "Age": 35})
    assert not schema.is_valid({
        "Greet": None,
        "Friends": None,
        "Age": None})
