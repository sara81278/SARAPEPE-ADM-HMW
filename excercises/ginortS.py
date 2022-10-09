# Enter your code here. Read input from STDIN. Print output to STDOUT

def customSort(string):
    outputList = []
    evenDig = []
    oddDig = []
    lower = []
    upper = []
    
    for c in string:
        if(c.islower()):
            lower.append(c)
        if(c.isdigit()):
            if(int(c)%2 == 0):
                evenDig.append(c)
            else:
                oddDig.append(c)
        if(c.isupper()):
            upper.append(c)
            
    outputList.extend(sorted(lower))
    outputList.extend(sorted(upper))
    outputList.extend(sorted(oddDig))
    outputList.extend(sorted(evenDig))
    return ''.join(outputList)

if __name__ == '__main__':
    print(customSort(input()))    
    
