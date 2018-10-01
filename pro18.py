print("displaying a armstrong number between 2 intervals")
b=int(input("begin="))
e=int(input("end="))
for x in range(b+1,e):
s=0
a=0
t=x
while x>0:
re=x%10
a=re**s
s=s+a
x=x//10
if(t==s)
print(s)
