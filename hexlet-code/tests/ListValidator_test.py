from validator.Validator import Validator

v_list1 = Validator().list().required()
v_list2 = Validator().list()

def required_test():
    assert v_list1.is_valid([]) == True
    assert v_list1.is_valid(None) == False
    assert v_list1.is_valid(['Test']) == True
    assert v_list2.is_valid(None) == True
    assert v_list2.is_valid([]) == True
    assert v_list2.is_valid(["Test"]) == True


def sizeof_test():
    assert v_list1.sizeof(4).is_valid([1, 2, 3, 4]) == True
    assert v_list1.sizeof(55).sizeof(2).is_valid(["Hexlet", "tests"]) == True
    assert v_list2.sizeof(0).is_valid(None) == True
    try:
        v_list2.sizeof('test')
    except TypeError:
        print("Error test done")




required_test()
sizeof_test()
