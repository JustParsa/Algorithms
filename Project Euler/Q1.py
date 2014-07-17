num = 0
sum_total = 0

while num < 1000:
	if num % 3 == 0 or num % 5 == 0:
		sum_total += num
		print num, sum_total
	num += 1

print sum_total
