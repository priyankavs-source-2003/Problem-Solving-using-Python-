'''Diwali party
Max is planning to take part in a Diwali contest at a Diwali Party that will begin at 8 PM and will
run until midnight (12 AM) l.e., for 4 hours. He also needs to travel to the party venue within this
time which takes him P minutes. The contest comprises of N problems that are arranged in order of
difficulty, with problem 1 being the simplest and problem N being the most difficult. Max is aware
that he will require 5*1 minutes to solve the problem.
Your task is help Max find and return an integer value, representing the number of problems Max
can solve and reach the party venue within the given time frame of 4 hours.
Note: Max will leave his home at exactly B PM to reach the party venue.
Input Format:
Input: An integer value N, representing the total number of problems.
Input2: An integer value P, Representing the time to travel in minutes from his home to the party
venue. '''


n=int(input('total no. of problems '))
p=int(input('time to travel from his home to part venue '))
t=240
count=0
sum=0
for i in range(1,n+1):
    prob=5*i   #print(prob)
    sum=sum+prob
    
    if sum<(t-p):
        count=count+1
#print("sum=",sum)
print("count=",count)


#or


n=int(input('total no. of problems '))
p=int(input('time to travel from his home to part venue '))
time_left=240-p
count=0
for i in range(1,n+1):
    if time_left>0 and time_left>5*i:
        time_left=time_left-5*i
        count=count+1
    else:
        break
print(count)