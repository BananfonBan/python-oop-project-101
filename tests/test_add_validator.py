from validator.Validator import Validator


def test_1():
    v = Validator()

    def fn(value, start):
        return value.startswith(start)

    v.add_validator('string', 'startWith', fn)
    schema = v.string().test('startWith', 'H')

    assert not schema.is_valid('exlet')
    assert schema.is_valid('Hexlet')

    def fn_2(value, _min):
        return value >= _min
    v.add_validator('number', 'min', fn_2)
    schema = v.number().test('min', 5)

    assert not schema.is_valid(4)
    assert schema.is_valid(6)


def test_2():
    def key_is_str(dict):
        for key in dict.keys():
            if type(key) is not str:
                return False
        return True

    v = Validator()
    v.add_validator("dict", "key is str", key_is_str)
    schema = v.dict().test("key is str")

    assert schema.is_valid({"key": "test", "some": 42})
    assert not schema.is_valid({"key": "test", 42: 42})

    def value_is_number(dict):
        for value in dict.values():
            if type(value) is not int and type(value) is not float:
                return False
        return True

    v = Validator()
    v.add_validator("dict", "value is number", value_is_number)
    v.add_validator("dict", "key is str", key_is_str)
    schema = v.dict().shape({
        "new validator": v.dict().test("value is number").test("key is str"),
        "common validator": v.string().required().contains("!")
    })

    assert schema.is_valid({
        "new validator": {"42": 42, "69": 69, "72": 72},
        "common validator": "It string!"})
    assert not schema.is_valid({
        "new validator": {"42": 42, "69": 69, "72": 72},
        "common validator": "It string but..."})
    assert not schema.is_valid({
        "new validator": {42: 42, "69": 69, "72": 72},
        "common validator": "It string but!"})
    assert not schema.is_valid({
        "new validator": {"42": "!42!", "69": 69, "72": 72},
        "common validator": "It string but!"})
