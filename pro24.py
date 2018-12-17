def smallest(arr,n):
min=arr[0]
for i in range(1,n):
if arr[i]>min:
min=arr[i]
sort in wave(arr,n)
return min
arr=[10,245,56,89]
n=len(arr)
ans=smallest (arr,n)
print("answer",ans)
