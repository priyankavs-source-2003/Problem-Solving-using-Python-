'''Fellis Function

Morris Fellis has come up with a new function called Fellis function Morris defines the function as
follows:
f(0) = 1
f(1) = 1
f(N)=f(N-1)+7^ * f(N - 2) + (N / 4) modulo 10 ^9+ 7
Given an integer N, your task is to help Morris find and return an Integer value of f(N), after
performing Fellis Function.
Note: Here the division operator is integer division operator le, it divides two numbers and returns
the integer part of the result
Input Specification:
Input1: An integer. Value N representing the fellis function value  '''

def f(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
       return (f(n-1)+7*f(n-2)+(n//4) %(10**9+7))

 

n=int(input())
print(f(n))