import string
class PhoneNumber:
    def __init__(self, number):
         self.number = self._validate(number)
         self.area_code = self.number[0:3]
         self.exchange = self.number[3:6]
         self.subscriber = self.number[6:10]
         
    def _validate(self, number):
        digits = "".join(char for char in number if char.isdigit())
        remaining = {char for char in number if not (char.isdigit() or char.isalpha())}
        valid_formatting = ' ()-.+'
        
        if any(char.isalpha() for char in number):
            raise ValueError("letters not permitted")
        if remaining.difference(valid_formatting):
            raise ValueError("punctuations not permitted")
        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits) > 11:
           raise ValueError("must not be greater than 11 digits")
        if len(digits) == 11:
           if digits[0] != '1':
             raise ValueError("11 digits must start with 1")
           digits = digits[1:]
        if digits[0] == '0':
           raise ValueError("area code cannot start with zero")
        if digits[0] == '1':
           raise ValueError("area code cannot start with one")
        if digits[3] == '0':
           raise ValueError("exchange code cannot start with zero")
        if digits[3] == '1':
           raise ValueError("exchange code cannot start with one")
        return digits

    def pretty(self):
        return f"({self.area_code})-{self.exchange}-{self.subscriber}"