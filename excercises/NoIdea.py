# Enter your code here. Read input from STDIN. Print output to STDOUT

def computeHappiness(array, likeSet, dislikeSet):
    happiness = sum([1 for i in array if i in likeSet])
    happiness = happiness - sum([1 for i in array if i in dislikeSet])
    return happiness
    
if __name__ == '__main__':
    n, m = input().split()
    array = input().split()
    likeSet = set(input().split())
    dislikeSet = set(input().split())
    print(computeHappiness(array, likeSet, dislikeSet))    
