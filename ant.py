'''    Ant on rail
There is a ant on your balcony.It wants to leave the rail so sometimes it moves right and
sometimes it moves left until it gets exhausted.Given an integer array A of size N which
consists of integer 1 and -1 only representing ant's moves.Where 1 means ant moved unit distance
towards the right side and -1 means it moved unit
distance towards the left .Your task is to find and return the integer value representing how
many times the ant reaches back to original starting position.
Note:
• Assume 1-based indexing
• Assume that the railing extends infinitely on the either sides
Input Format:
input1 : An integer value N representing the number of moves made by the ant. input2 :
An integer array A consisting of the ant's moves towards either side Sample Input
5
1 -1 1 -1 1
Sample Output:
2       '''

move=int(input("enter the number of ants moves:"))
ant_move=list(map(int,input("enter ant's moves: ").split()))
start=0
count=0
for move in ant_move:
    start+=move
    if start==0:
        count+=1
print("count=",count)

#or

array=list(map(int,input().split()))
n=len(array)

count=0
for i in range(n):
    if sum(array[:i+1])==0:
        count=count+1
print(count)    

