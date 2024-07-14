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


def add_validator_test():
    def in_list(list_, values_1, values_2):
        return values_1 in list_ and values_2 in list_
    
    v = Validator()
    v.add_validator("list", "in list", in_list)
    schema = v.list().test("in list", 42, 69)
    assert schema.is_valid([1, 42, 55, 69]) == True
    assert schema.is_valid([1, 42, 55]) == False
    schema2 = v.list().test("in list", 42, 69).sizeof(5)
    assert schema2.is_valid([2, 34, 42, 77, 69]) == True
    assert schema2.is_valid([2, 34, 42, 77, 59]) == False




required_test()
sizeof_test()
add_validator_test()
