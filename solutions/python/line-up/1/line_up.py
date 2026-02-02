def line_up(name, number):
    if str(number) == '1' or len(str(number)) > 1 and str(number)[-2] != '1' and str(number)[-1] == '1':
        return f'{name}, you are the {number}st customer we serve today. Thank you!'
    elif str(number) == '2' or len(str(number)) > 1 and str(number)[-2] != '1' and str(number)[-1] == '2':
        return f'{name}, you are the {number}nd customer we serve today. Thank you!'
    elif str(number) == '3' or len(str(number)) > 1 and str(number)[-2] > '1' and str(number)[-1] == '3':
        return f'{name}, you are the {number}rd customer we serve today. Thank you!'
    else:
        return f'{name}, you are the {number}th customer we serve today. Thank you!'