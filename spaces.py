'''  Space counter

You have been gives the task of making the counter on a social media platform more userfriendly.your task is to find and return an integer value representing the count of the number of
spaces in a gives string S.
Input:
A string:
Output:
Return an integer value representing the count of the number of space in a given string S.'''

sentence=input(print("enter any sentence:"))
for i in sentence:
    spaces=sentence.count(" ")
print("number of spaces : ",spaces)

