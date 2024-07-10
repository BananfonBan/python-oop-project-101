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
    "Friends":v.list().sizeof(2),
    "Age": v.number().positive().range(14, 120)
})

def dictvalidator_test(schema):
    assert schema.is_valid({'name': 'kolya', 'age': 100}) == True
    assert schema.is_valid({'name': 'maya', 'age': None}) == False
    assert schema.is_valid({'name': '', 'age': None}) == False
    assert schema.is_valid({'name': 'ada', 'age': -5}) == False


def dictvalidator_test2(schema):
    assert schema.is_valid({"Greet": "Hello Bob!", "Friends": ["Dima", "Lesha"], "Age": 42}) == True
    assert schema.is_valid({"Greet": "Goodby", "Friends": ["Bob"], "Age": -8}) == False
    assert schema.is_valid({"Greet": "Hello Maks!", "Friends": ["Sahsa", "Ron"], "Age": 8}) == False
    assert schema.is_valid({"Greet": "Hello Gerda", "Friends": [], "Age": 35}) == False
    assert schema.is_valid({"Greet": "Hello", "Friends": ["Vity", "Grisha"], "Age": 35}) == False
    assert schema.is_valid({"Greet": "Hello Grisha", "Friends": ["Pasha", "Iliy"], "Age": 35}) == True

    
dictvalidator_test(schema)
dictvalidator_test2(schema2)