from validator.Validator import Validator

v_num1 = Validator().number()
v_num2 = Validator().number()


def requred_test():
    v_num1 = Validator().number()
    v_num2 = Validator().number()
    assert v_num1.positive().is_valid(None)
    assert not v_num1.required().is_valid(None)
    assert not v_num1.is_valid(None)
    assert v_num1.is_valid(1)
    assert v_num2.is_valid(None)
    assert v_num2.is_valid(0)


def range_test():
    v_num1 = Validator().number().required()
    v_num2 = Validator().number()
    assert v_num1.range(-5, 5).is_valid(0)
    assert v_num1.is_valid(-5)
    assert not v_num1.is_valid(10)
    assert not v_num1.is_valid(None)
    assert v_num2.range(0, 10).is_valid(10)
    assert not v_num2.is_valid(100)
    assert v_num2.is_valid(None)
    assert v_num1.range(0, 10).range(-10, 5).is_valid(-4)


def positive_test():
    v_num1 = Validator().number().required()
    v_num2 = Validator().number()
    assert not v_num1.positive().is_valid(-5)
    assert v_num1.is_valid(4)
    assert not v_num1.is_valid(None)
    assert v_num2.positive().is_valid(4)
    assert v_num2.positive().is_valid(None)


def add_validator_test():
    v = Validator()

    def non_positive(num):
        return num <= 0

    v.add_validator("number", "not positive", non_positive)
    schema = v.number().test("not positive")
    assert schema.is_valid(-4)
    assert not schema.is_valid(5)
    assert not schema.range(-10, -5).is_valid(-4)
    assert schema.range(-10, -5).is_valid(-7)


requred_test()
range_test()
positive_test()
add_validator_test()
