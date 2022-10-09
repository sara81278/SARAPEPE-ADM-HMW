def isanyalnum(s):
    output = sum([1 for c in s if c.isalnum()])
    return output>0

def isanyalpha(s):
    output = sum([1 for c in s if c.isalpha()])
    return output>0

def isanylower(s):
    output = sum([1 for c in s if c.islower()])
    return output>0

def isanydigits(s):
    output = sum([1 for c in s if c.isdigit()])
    return output>0

def isanyupper(s):
    output = sum([1 for c in s if c.isupper()])
    return output>0

if __name__ == '__main__':
    s = input()
    print(isanyalnum(s))
    print(isanyalpha(s))
    print(isanydigits(s))
    print(isanylower(s))
    print(isanyupper(s))
