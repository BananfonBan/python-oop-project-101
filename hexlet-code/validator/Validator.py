class Validator:
    def __init__(self):
        self.is_required = False


    def is_valid(self, obj):
        pass


    def required(self):
        self.is_required = True


    def string(self):
        return String_Validator()
    


class String_Validator(Validator):
    def __init__(self):
        super().__init__()
        self.min_length = -float('inf')
        self.contain = ''


    def required(self):
        self.is_required = True
        return self


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
