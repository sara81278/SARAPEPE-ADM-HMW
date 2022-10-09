def swap_case(s):
    result = ''
    for letter in s:
        if(letter.isupper()):
            result = result + letter.lower()
        else:
            result = result + letter.upper()
    return result

