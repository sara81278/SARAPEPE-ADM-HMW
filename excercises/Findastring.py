##Here I could've just used string.count(sub_string),
##but I think the purpose of the exercise it's not just
##to use built-in functions, so I implemented the logic myself.
def count_substring(string, sub_string):
    stringLen = len(string)
    subStringLen = len(sub_string)

    count = sum([1 for i in range(0, stringLen-subStringLen+1)
    if(string[i:subStringLen+i]==sub_string)])
    
    return count

