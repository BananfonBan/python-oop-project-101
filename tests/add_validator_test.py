from validator.Validator import Validator


def test_1():
    v = Validator()
    fn = lambda value, start: value.startswith(start)
    v.add_validator('string', 'startWith', fn)
    schema = v.string().test('startWith', 'H')

    assert schema.is_valid('exlet') == False
    assert schema.is_valid('Hexlet') == True

    fn = lambda value, min: value >= min
    v.add_validator('number', 'min', fn)
    schema = v.number().test('min', 5)

    assert schema.is_valid(4) == False
    assert schema.is_valid(6) == True


def test_2():
    def key_is_str(dict):
        for key in dict.keys():
            if type(key) != str:
                return False
        return True

    v = Validator()
    v.add_validator("dict", "key is str", key_is_str)
    schema = v.dict().test("key is str")

    assert schema.is_valid({"key": "test", "some": 42}) == True
    assert schema.is_valid({"key": "test", 42: 42}) == False

    def value_is_number(dict):
        for value in dict.values():
            if type(value) != int and type(value) != float:
                return False
        return True
    
    v = Validator()
    v.add_validator("dict", "value is number", value_is_number)
    v.add_validator("dict", "key is str", key_is_str)
    schema = v.dict().shape({
        "new validator": v.dict().test("value is number").test("key is str"),
        "common validator": v.string().required().contains("!")
    })

    assert schema.is_valid({"new validator": {"42": 42, "69": 69, "72": 72},
                            "common validator": "It string!"}) == True
    assert schema.is_valid({"new validator": {"42": 42, "69": 69, "72": 72},
                            "common validator": "It string but..."}) == False
    assert schema.is_valid({"new validator": {42: 42, "69": 69, "72": 72},
                            "common validator": "It string but!"}) == False
    assert schema.is_valid({"new validator": {"42": "!42!", "69": 69, "72": 72},
                              "common validator": "It string but!"}) == False


test_1()
test_2()