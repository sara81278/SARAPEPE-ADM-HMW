if __name__ == '__main__':
    n,m = map(int,input().split())
    pattern = '.|.'
    i = 1
    
    for row in range((n-1)//2): 
        print((pattern*(row+i)).center(m,'-'))
        i = i + 1
        
    print('WELCOME'.center(m,'-'))
    
    i = (n-1)//2 - 1
    for row in range((n-1)//2,0,-1):   
        print((pattern*(row+i)).center(m,'-'))
        i = i-1
