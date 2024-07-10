from Validator import Validator

v = Validator()

def required_string_test():
    assert v.string().is_valid('') == True
    assert v.string().required().is_valid(" ") == True



required_string_test()


__all__ = ('Validator',)