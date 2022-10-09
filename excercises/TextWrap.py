

def wrap(string, max_width):
    result = ''
    for i in range(0, len(string), max_width):
        result = result + string[i:i+max_width] + '\n'
    if(not result):
        result = string
    return result

