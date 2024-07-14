from validator.Validator import Validator

v = Validator()

schema = v.dict()

schema.shape({
    'name': v.string().required(),
    'age': v.number().positive(),
})

schema2 = v.dict()

schema2.shape({
    "Greet": v.string().min_len(6).contains('Hello'),
    "Friends": v.list().sizeof(2),
    "Age": v.number().positive().range(14, 120)
})

schema3 = v.dict()

schema3.shape({
    "Greet": v.string().required().min_len(6).contains('Hello'),
    "Friends": v.list().required().sizeof(2),
    "Age": v.number().required().positive().range(14, 120)
})


def dictvalidator_test(schema):
    assert schema.is_valid({'name': 'kolya', 'age': 100})
    assert schema.is_valid({'name': 'maya', 'age': None})
    assert not schema.is_valid({'name': '', 'age': None})
    assert not schema.is_valid({'name': 'ada', 'age': -5})


def dictvalidator_test2(schema):
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


def dictvalidator_test3(schema):
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


dictvalidator_test(schema)
dictvalidator_test2(schema2)
dictvalidator_test3(schema3)
