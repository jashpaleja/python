t=int(input())
li=[]
pp=0
def cake():
	x=input()
	x=x.split(' ')
	for i in range(len(x)):
		x[i]=int(x[i])
	s=x[0]
	n=x[1]
	k=x[2]
	r=x[3]
	tot=k
	for i in range(n-1):
		k=k*r
		tot=tot+k
	return s-tot
for i in range(t):
	li.append(cake())
for i in li:
	if i<0:
		print("IMPOSSIBLE "+ str(abs(i)))
	else:
		print("POSSIBLE "+ str(i))
pp=sum(li)
if pp<0:
	print("IMPOSSIBLE")
else:
	print("POSSIBLE")