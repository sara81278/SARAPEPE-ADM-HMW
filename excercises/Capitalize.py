

# Complete the solve function below.
def solve(s):
    result = s[0].upper()
    for i in range(0, len(s)-1):
        if(s[i] == ' '):
            result = result + s[i+1].upper()
        else:
            result = result + s[i+1]
    return result

