''' Reverse the order of string:

You are given a string containing words separated by space.your task is to write a function or
program that reverses the order of words in the string '''

s=input().split()
s=s[::-1]
print(*s,sep=" ") 