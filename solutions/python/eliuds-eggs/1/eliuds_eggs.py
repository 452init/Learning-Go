def egg_count(display_value):
    string = ''
    while (display_value > 0):
        rem = display_value % 2
        string = str(rem) + string
        display_value = display_value//2
    egg_no = [(int(n)) for n in string if n == '1']
    return sum(egg_no)