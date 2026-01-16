import string

class PhoneNumber:
    def __init__(self, number):
        if any(char.isalpha() for char in number):
            raise ValueError("letters not permitted")
        
        digits = ''.join(char for char in number if char.isdigit())

        remaining = ''.join(char for char in number if not char.isdigit() and not char.isalpha())
        valid_formatting = ' ()-.+'
        if any(char not in valid_formatting for char in remaining):
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
        self.number = digits
        self.area_code = digits[0:3]
        self.exchange = digits[3:6]
        self.subscriber = digits[6:10]
    
    def pretty(self):
        return f"({self.area_code})-{self.exchange}-{self.subscriber}"