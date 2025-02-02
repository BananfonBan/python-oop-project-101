from validator.Validator import Validator


def test_required_string():
    v_str = Validator().string()
    v_str2 = Validator().string()
    assert v_str != v_str2
    assert v_str.is_valid('')
    assert v_str.is_valid(None)
    assert v_str2.is_valid('')
    assert v_str2.is_valid(None)
    v_str.required()
    assert not v_str.is_valid(None)
    assert not v_str.is_valid("")
    assert v_str2.is_valid(None)
    assert v_str2.is_valid("")


def test_min_len():
    v_str = Validator().string().required()
    v_str2 = Validator().string()
    assert v_str.min_len(4).is_valid("Hello!")
    assert v_str2.min_len(4).is_valid(None)
    assert v_str2.min_len(4).is_valid("")
    assert v_str.min_len(10).min_len(4).is_valid("Hello World!")
    assert not v_str.min_len(10).is_valid("not")
    assert not v_str2.min_len(10).is_valid("not")


def test_contains():
    v_str = Validator().string().required()
    v_str2 = Validator().string()
    assert v_str.contains("World").is_valid("Hello World!")
    assert v_str2.min_len(5).is_valid("ABBA, BABA")
    assert not v_str2.min_len(5).is_valid("AB")
    assert v_str2.min_len(5).is_valid("")


def test_add_validator():
    def start_with(string, letter):
        return string[0] == letter
    v = Validator()
    v.add_validator("string", "start with", start_with)
    schema = v.string().test("start with", "H")
    assert schema.is_valid("Hexlet")
    assert not schema.is_valid("Exlet")
    assert schema.contains("let").min_len(5).is_valid("Hexlet let")
    assert not schema.contains("let").min_len(5).is_valid("HexHex")
