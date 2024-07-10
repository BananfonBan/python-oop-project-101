class Validator:
    def __init__(self):
        self.is_required = False


    def is_valid(self, obj):
        pass


    def required(self):
        self.is_required = True
        return self


    def string(self):
        return StringValidator()


    def number(self):
        return NumberValidator()


    def list(self):
        return ListValidator()


    def dict(self):
        return DictValidator()


class StringValidator(Validator):
    def __init__(self):
        super().__init__()
        self.min_length = -float('inf')
        self.contain = ''


    def contains(self, string):
        self.contain = string
        self.is_required = True
        return self


    def min_len(self, length:int=-float('inf')):
        self.min_length = length
        self.is_required = True
        return self


    def is_valid(self, string):
        if not self.is_required:
            return True
        elif string == None or string == '' and self.is_required:
            return False
        elif self.contain in string and len(string) >= self.min_length:
            return True
        else:
            return False
        

class NumberValidator(Validator):
    def __init__(self):
        super().__init__()
        self.is_positive_check = False
        self.min_value = -float('inf')
        self.max_value = float('inf')

    
    def positive(self):
        self.is_required = True
        self.is_positive_check = True
        return self
    

    def range(self, min_value:int, max_value:int):
        if min_value > max_value:
            raise ValueError("The minimum value must be less than the maximum" )
        else:
            self.is_required = True
            self.min_value = min_value
            self.max_value = max_value
            return self

        
    def is_valid(self, number):
        if not self.is_required:
            return True
        elif number == None or type(number) != int and self.is_required:
            return False
        elif self.min_value <= number <= self.max_value:
            if self.is_positive_check:
                return number > 0
            else:
                return True
        else:
            return False 


class ListValidator(Validator):
    def __init__(self):
        super().__init__()
        self.sizeof_list = None


    def sizeof(self, value:int):
        if type(value) != int:
            raise TypeError("Size of list must be integer value")
        self.sizeof_list = value
        self.is_required = True
        return self
    

    def is_valid(self, obj):
        if not self.is_required:
            return True
        elif type(obj) == list:
            if self.sizeof_list == None:
                return True
            else:
                return len(obj) == self.sizeof_list
        else:
            return False
        

class DictValidator(Validator):
    def __init__(self):
        super().__init__()
        self.dict_shape = {}


    def shape(self, dict_shape:dict):
        self.dict_shape = dict_shape
        return self


    def is_valid(self, obj:dict):
        if type(obj) != dict:
            raise TypeError("Value must be dictionary")
        if obj.keys() != self.dict_shape.keys():
            raise ValueError("Keys of shape dict and dict must be the same")
        for key, value in obj.items():
            if not self.dict_shape[key].is_valid(value):
                return False
        return True
        




