from validator.Validator import Validator

vlist1 = Validator().list().required()
vlist2 = Validator().list()

def required_test():
    assert vlist1.is_valid([]) == True
    assert vlist1.is_valid(None) == False
    assert vlist1.is_valid(['Test']) == True
    assert vlist2.is_valid(None) == True
    assert vlist2.is_valid([]) == True
    assert vlist2.is_valid(["Test"]) == True


def sizeof_test():
    assert vlist1.sizeof(4).is_valid([1, 2, 3, 4]) == True
    assert vlist1.sizeof(55).sizeof(2).is_valid(["Hexlet", "tests"]) == True
    assert vlist2.sizeof(0).is_valid([]) == True
    try:
        vlist2.sizeof('test') == ValueError
    except ValueError:
        print("Error test done")




required_test()
sizeof_test()
