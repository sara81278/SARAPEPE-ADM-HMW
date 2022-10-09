def print_formatted(number):
    l = len(format(n, 'b'))
    for i in range(1,number+1):
        print(str(i).rjust(l), format(i,'o').rjust(l), format(i,'X').upper().rjust(l),format(i,'b').rjust(l), sep=' ')

