num=int(input("enter the no of digits you want in series(minimum 2):")
first=0
second=1
print("\n fibonacci series is:")
print(first,",",second,end=",")
for i in range(2,num):
next=first+second
print(next,end=",")
first=second
second=next
