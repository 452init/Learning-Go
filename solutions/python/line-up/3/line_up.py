def line_up(name, number):

    suffix = ["th", "st", "nd", "rd"]
    if len(str(number))>1 and str(number)[-2] != '1' and str(number)[-1] != '0' or number < 4:
        if str(number)[-1] == '1':
            suffix = suffix[1]
        elif str(number)[-1] == '2':
            suffix = suffix[2]
        elif str(number)[-1] == '3':
            suffix = suffix[3]
    else:
        suffix = suffix[0]
    return f'{name}, you are the {number}{suffix} customer we serve today. Thank you!'