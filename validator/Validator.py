class ValidatorBase:
    def __init__(self):
        self.is_required = False
        self.checks = {}


    def required(self):
        pass


    def test(self, name_validator, *value):
        self.checks.update({name_validator: {"func": self.validators[name_validator], "args": list(value)}})
        return self


    def is_valid(self, obj):
        if not self.is_required and not self._required(obj):
            return True
        elif self.is_required and not self._required(obj):
            return False
        for key, value in self.checks.items():
            if self.validators[key](obj, *value["args"]) == False:
                return False
        return True



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


    def list(self):
        return ListValidator(validators=self.user_validators["list"])


    def dict(self):
        return DictValidator(validators=self.user_validators["dict"])


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



class ListValidator(ValidatorBase):
    def __init__(self, validators):
        super().__init__()
        self.validators = {
            "required": self._required,
            "sizeof": self._sizeof,
        }
        self.validators.update(validators)


    @staticmethod
    def _required(list_):
        return type(list_) == list


    @staticmethod
    def _sizeof(list_, value):
        return len(list_) == value


    def required(self):
        self.is_required = True
        self.checks.update({"required": {"func": self._required, "args": []}})
        return self


    def sizeof(self, value:int):
        self.checks.update({"sizeof": {"func":self._sizeof, "args": [value]}})
        return self


class DictValidator(ValidatorBase):
    def __init__(self, validators):
        super().__init__()
        self.validators = {
            "requierd": self._required,
            "shape": self._shape
        }
        self.validators.update(validators)


    @staticmethod
    def _shape(_dict, dict_shape):
        for key, value in _dict.items():
            if not dict_shape[key].is_valid(value):
                return False
        return True


    @staticmethod
    def _required(_dict):
        return type(_dict) == dict


    def shape(self, dict_shape:dict):
        self.checks.update({"shape": {"func": self._shape, "args": [dict_shape]}})
        return self
