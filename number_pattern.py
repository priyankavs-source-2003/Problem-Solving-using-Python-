'''Pattern

Print the given pattern
You are given a number n and you have to print the given pattern:
For n=3
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1   ''' 

def pattern(n):
    for i in range(n,0,-1):
        a=[]
        for j in range(n,0,-1):
            a+=[j]*i
           
        print(*a,sep=' ',end=' ')
        print()
n=3
pattern(n)