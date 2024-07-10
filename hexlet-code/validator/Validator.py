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
        if self.is_required == False:
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
        if self.is_required == False:
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


