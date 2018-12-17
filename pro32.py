frame=input("enter the file name:")
num-words=0
with open(f name,'r')as f:
for line in f:
words=line.split()
num-words+=len(words)
print("number of words:")
print(num-words)
