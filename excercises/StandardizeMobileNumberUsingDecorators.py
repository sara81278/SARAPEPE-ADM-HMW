def wrapper(f):
    def fun(l):
        output = []
        for el in l:
            i = 2
            if(el[0] == '0'):
                i = 1
            elif(len(el)==10):
                i = 0
            output.append('+91 '+el[-10:-5]+' '+el[-5:])
        return f(output)
    return fun

