def isPrime (number):
	for div in range (2, int(number**0.5)+1):
		if number % div == 0:
			return False
	return True

nth_Prime = 0
num = 1 
while nth_Prime != 10001:
	num += 1	
	if isPrime (num) == True:
		nth_Prime += 1

print "\n",num, nth_Prime

