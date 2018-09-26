print("check whether a number is prime or not")
N=int(input("number="))
flag=0
for x in range(1,N+1):
if(N%X==0):
flag=flag+1
if(flag==2):
print("prime"0
else:
print("not a prime")
