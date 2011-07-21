import math
def factors(n):
	s=0	
	k = int(math.sqrt(n))
	for i in range(k,0,-1):
		if n % i == 0:
			s = s+1
	if n == pow(k,2):
		return 2*s-1
	else:	
		return 2*s

a,b,f = 1,2,3
while f < 500:
	a,b = a+1,b+1
	if a%2==0:
		f = factors(a/2)*factors(b)-1
	else:
		f = factors(a)*factors(b/2)-1

print "The Number = ",(a*b)/2," and Number of Factors=",f
