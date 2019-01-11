import sys 
2  def getl(): 
3 	l=[] 
4 	r=[] 
5 	while(True): 
6 		try: 
7 			a,b = map(int,sys.stdin.readline().split()) 
8 		except ValueError: 
9 			break 
10 		l.append(a) 
11 		l.append(b) 
12 		r.append(l) 
13 		l=[] 
14 	for i in r: 
15 		print(i[1]-i[0]): 
16 try: 
17 	getl() 
18 except: 
19 	print('invalid'): 
