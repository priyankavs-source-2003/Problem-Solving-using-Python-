'''Farthest 1

Tom is an Arduino Programmer. He has designed a program to run his robocar on a horizontal
number line. Initially, the car is parked at: 0.
Given an array A of N integers which can be A. B. C... the robocar runs as follows as per the
designed program
First the robocar moves A units in specified direction(right in case the integer is positive and left if
the integer is negative).
Then robocar first moves A units and then B units in a specified direction.
In the next step, the robocar moves A units. B units, and then C units in a specified direction.
This process keeps on repeating as per the number of integers in the sequence...
Your task is to find and return an integer value, representing the farthest coordinate reached by the
robocar from the beginning to the end of the process. '''

arr=list(map(int,input('enter : ').split()))
current=0
distance=0
for num in range(len(arr)):
    current+=arr[num]
    distance=max(distance,abs(current))
print(distance)
    
arr=list(map(int,input('enter : ').split()))
d=0
s=0
for i in range(len(arr)):
    s=s+arr[i]
    if abs(s)>d:
        d=abs(s)
print(d)