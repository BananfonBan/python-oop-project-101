class ValidatorBase:
    def __init__(self):
        self.is_required = False
        self.checks = {}


    def is_valid(self, obj):
        pass


    def required(self):
        pass


    def test(self, name_validator, *value):
        self.checks.update({name_validator: {"func": self.validators[name_validator], "args": list(*value)}})
        return self



class Validator:
    def __init__(self):
        self.user_validators = {
            "string": {},
            "number": {},
            "list": {},
            "dict": {},
        }


    def string(self):
        return StringValidator(validators=self.user_validators["string"])


    def number(self):
        return NumberValidator(validators=self.user_validators["number"])


    # def list(self):
    #     return ListValidator()


    # def dict(self):
    #     return DictValidator()


    def add_validator(self, type_validator:str, name_validator:str, fn):
        if not type_validator in self.user_validators:
            raise ValueError("Valid values of type validators:\nstring\nnumber\nlist\ndict")
        new_fn = {name_validator: fn}
        self.user_validators[type_validator].update(new_fn)



class StringValidator(ValidatorBase):
    def __init__(self, validators):
        super().__init__()
        self.validators = {
            "required": self._required,
            "contains": self._contains,
            "min len": self._min_length,
        }
        self.validators.update(validators)


    @staticmethod
    def _required(string):
        return string != None and string != ""


    @staticmethod
    def _contains(string, сontained_string):
        return сontained_string in string


    @staticmethod
    def _min_length(string, min):
        return len(string) >= min


    def required(self):
        self.is_required = True
        self.checks.update({"required":{"func":self._required, "args": []}})
        return self


    def contains(self, string):
        self.checks.update({"contains": {"func":self._contains, "args": [string]}})
        return self


    def min_len(self, length:int=-float('inf')):
        self.checks.update({"min len": {"func":self._min_length, "args": [length]}})
        return self


    def is_valid(self, string):
        if not self.is_required and (string == None or string == ''):
            return True
        for key, value in self.checks.items():
            if self.validators[key](string, *value["args"]) == False:
                return False
        return True



class NumberValidator(ValidatorBase):
    def __init__(self, validators):
        super().__init__()
        self.validators = {
            "required": self._required,
            "positive": self._positive,
            "range": self._range,
        }
        self.validators.update(validators)


    @staticmethod
    def _required(num):
        return type(num) == int
    

    @staticmethod
    def _positive(num):
        return num > 0

    
    @staticmethod
    def _range(num, min, max):
        return min <= num <= max


    def required(self):
        self.is_required = True
        self.checks.update({"required":{"func":self._required, "args": []}})
        return self

    def positive(self):
        self.checks.update({"positive": {"func": self._positive, "args": []}})
        return self


    def range(self, min_value:int, max_value:int):
        self.checks.update({"range": {"func": self._range, "args": [min_value, max_value]}})
        return self


    def is_valid(self, number):
        if not self.is_required and type(number) != int:
            return True
        for key, value in self.checks.items():
            if self.validators[key](number, *value["args"]) == False:
                return False
        return True


class ListValidator(ValidatorBase):
    def __init__(self):
        super().__init__()
        self.type_validator = "list"
        self.sizeof_list = None


    def sizeof(self, value:int):
        if type(value) != int:
            raise TypeError("Size of list must be integer value")
        self.sizeof_list = value
        return self


    def is_valid(self, obj):
        if not self.is_required and type(obj) != list:
            return True
        elif type(obj) == list:
            if self.sizeof_list:
                return len(obj) == self.sizeof_list
            else:
                return True
        else:
            return False


class DictValidator(ValidatorBase):
    def __init__(self):
        super().__init__()
        self.type_validator = "dict"
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

