if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    xlist= [i for i in range (0,x+1)]
    ylist = [i for i in range (0,y+1)]
    zlist = [i for i in range (0,z+1)]
    a = [[i,k,j] for i in xlist for k in ylist for j in zlist if (i+k+j)!=n ]
    print(a)
