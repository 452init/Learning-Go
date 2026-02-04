def line_up(name, number):
    if len(str(number))>1 and str(number)[-2] != '1' and str(number)[-1] != '0' or number < 4:
        if str(number)[-1] == '1':
            suffix = 'st'
        elif str(number)[-1] == '2':
            suffix = 'nd'
        elif str(number)[-1] == '3':
            suffix = 'rd'
    else:
        suffix = 'th'
    return f'{name}, you are the {number}{suffix} customer we serve today. Thank you!'