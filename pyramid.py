'''Pyramid sum
Adam has a pyramid of numbers. The pyramid structure is formed by arranging the numbers in the
following pattern
1
 212
 32123
 4321234
 543212345
N__212__N
• The first row contains the number 1. The second row contains the numbers 2, 1, and 2. The third
row contains the numbers 3, 2, 1, 2, and 3. This pattern continues for subsequent rows, until it
reaches N, which represents the height of the pyramid.
• Given height of pyramid N find the sum of the numbers in the pyramid and return the sum as the
output.
Sample input:
3
Sample output:
17  '''

n=int(input("enter height of pyramid:"))
res=n*1
num=2
for i in range(n-1,0,-1):
    res+=2*num*i
    num+=1

print(res)