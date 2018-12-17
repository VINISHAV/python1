def merge-sort(seq)
if len(seq)==1:
return seq
left=merge-sort(seq[:len(seq)])
right=merge-sort(seq[:len(seq)])
return merge(left,right)
