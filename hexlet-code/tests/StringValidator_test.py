from validator.Validator import Validator

v_str = Validator().string()
v_str2 = Validator().string()


def required_string_test():
    assert v_str != v_str2
    assert v_str.is_valid('') == True
    assert v_str.is_valid(None) == True
    assert v_str2.is_valid('') == True
    assert v_str2.is_valid(None) == True
    v_str.required()
    assert v_str.is_valid(None) == False
    assert v_str.is_valid("") == False
    assert v_str2.is_valid(None) == True
    assert v_str2.is_valid("") == True


def min_len_test():
    assert v_str.min_len(4).is_valid("Hello!") == True
    assert v_str2.min_len(4).is_valid(None) == True
    assert v_str2.min_len(4).is_valid("") == True
    assert v_str.min_len(10).min_len(4).is_valid("Hello World!") == True
    assert v_str.min_len(10).is_valid("not") == False
    assert v_str2.min_len(10).is_valid("not") == False


def contains_test():
    assert v_str.contains("World").is_valid("Hello World!") == True
    assert v_str2.min_len(5).is_valid("ABBA, BABA") == True
    assert v_str2.min_len(5).is_valid("AB") == False
    assert v_str2.min_len(5).is_valid("") == True


def add_validator_test():
    def start_with(string, letter):
        return string[0] == letter
    v = Validator()
    v.add_validator("string", "start with", start_with)
    schema = v.string().test("start with", "H")
    assert schema.is_valid("Hexlet") == True
    assert schema.is_valid("Exlet") == False
    print(schema.is_valid("Hex"))


required_string_test()
min_len_test()
contains_test()
add_validator_test()


__all__ = ('Validator',)