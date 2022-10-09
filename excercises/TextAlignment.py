# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

print('\n'.join([((2*k+1)*'H').center(2*n-1) for k in range(n)]))
    
print('\n'.join([((n-1)//2)*' '+ (n*'H') + 3*n*' '+(n*'H') for k in range(n+1)]))

print('\n'.join([(((n-1)//2)*' '+(5*n)*'H') for k in range((n+1)//2)]))

print('\n'.join([((n-1)//2)*' '+ (n*'H') + 3*n*' '+(n*'H') for k in range(n+1)]))

print('\n'.join([((2*n-2*k-1)*'H').center(2*n-1).rjust(6*n-1) for k in range(n)]))
