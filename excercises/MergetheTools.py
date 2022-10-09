def merge_the_tools(string, k):
    output = [rmDup(string[i:i+k]) for i in range (0, len(string),k)]
    print(''.join(output))
    
    
def rmDup(string):
    output = ''
    for s in string:
        if (not s in output):
            output = output + s
    return output+'\n'

