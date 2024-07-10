from validator.Validator import Validator

vnum1 = Validator().number().required()
vnum2 = Validator().number()

def requred_test():
    assert vnum1.is_valid(None) == False
    assert vnum1.is_valid(0) == True
    assert vnum2.is_valid(None) == True
    assert vnum2.is_valid(0) == True


def range_test():
    assert vnum1.range(-5, 5).is_valid(0) == True
    assert vnum1.is_valid(-5) == True
    assert vnum1.is_valid(5) == True
    assert vnum1.is_valid(10) == False
    assert vnum2.range(0, 10).is_valid(10) == True
    assert vnum2.is_valid(100) == False



def positive_test():
    assert vnum1.positive().is_valid(-5) == False
    assert vnum1.is_valid(4) == True

try:
    vnum1.range(10, 5)
except ValueError as e:
    print("Error test done")

requred_test()
range_test()
positive_test()


