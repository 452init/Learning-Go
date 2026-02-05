def line_up(name, number):
    mapping = {'1': 'st', '2': 'nd', '3': 'rd'}
    suffix = mapping.get(str(number)[-1], 'th')
    if 11 <= number % 100 <= 13:
        suffix = 'th'
    return f'{name}, you are the {number}{suffix} customer we serve today. Thank you!'