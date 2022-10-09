def print_rangoli(size):
    for i in range(1,(size*2)):
        alpha='abcdefghijklmnopqrstuvwxyz'
        k = alpha[abs(size-i):size]
        k = k[-1:0:-1] + k
        print( '-'.join(k).center(4*size-3,'-'))

