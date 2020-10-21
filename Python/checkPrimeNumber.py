# check wheather no. is prime or not

n = 140
list=[]
for i in range(1,n+1):
	if n%i==0:
		list.append(i)
if(len(list))==2):
	print(n, 'is a prime number')
else:
	print(n, 'is not a prime number')
