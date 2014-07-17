#Recursive
# def fib (n):
# 	if n == 0 or n == 1: #change 0->1 and 1->2 for real fib (1,1,2,...)
# 		return 1
# 	return fib (n-1) + fib (n-2)    
# O(2^n)?

# Iterative
def fib (n):
	a = 1
	b = 1
	for x in range (1, n):
		temp = b
		b += a
		a = temp
	return b		#change b->a for real fib (1,1,2,...)
# O(n)?


i = 1
cur_fib = 0
total = 0
while cur_fib < 4000000:
	cur_fib = fib (i)
	print cur_fib
	if cur_fib % 2 == 0:
		total += cur_fib
	i += 1
print total


