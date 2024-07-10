from validator.Validator import Validator

v_str = Validator().string()

v_str2 = Validator().string()


def required_string_test():
    assert v_str != v_str2
    assert v_str.is_valid('') == True
    v_str.required()
    assert v_str.is_valid(None) == False
    assert v_str.is_valid("") == False
    assert v_str.min_len(4).is_valid("Hello!") == True
    assert v_str.min_len(10).min_len(4).is_valid("Hello World!") == True
    assert v_str.min_len(10).is_valid("not") == False
    assert v_str.contains("World").is_valid("Hello World!") == True
    assert v_str2.min_len(5).is_valid("ABBA, BABA") == True
    assert v_str2.min_len(5).is_valid("AB") == False




required_string_test()



__all__ = ('Validator',)