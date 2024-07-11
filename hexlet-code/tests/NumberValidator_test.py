from validator.Validator import Validator

v_num1 = Validator().number().required()
v_num2 = Validator().number()

def requred_test():
    assert v_num1.is_valid(None) == False
    assert v_num1.is_valid(0) == True
    assert v_num2.is_valid(None) == True
    assert v_num2.is_valid(0) == True


def range_test():
    assert v_num1.range(-5, 5).is_valid(0) == True
    assert v_num1.is_valid(-5) == True
    assert v_num1.is_valid(10) == False
    assert v_num1.is_valid(None) == False
    assert v_num2.range(0, 10).is_valid(10) == True
    assert v_num2.is_valid(100) == False
    assert v_num2.is_valid(None) == True



def positive_test():
    assert v_num1.positive().is_valid(-5) == False
    assert v_num1.is_valid(4) == True
    assert v_num1.is_valid(None) == False
    assert v_num2.positive().is_valid(4) == True
    assert v_num2.positive().is_valid(None) == True


try:
    v_num1.range(10, 5)
except ValueError as e:
    print("Error test done")

requred_test()
range_test()
positive_test()


