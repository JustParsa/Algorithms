boolNum = [True]*2000001

p = 2
sum = 2
while p <= 2000000:
	coefficient = 1
	while p*coefficient <= 2000000:
		boolNum[p*coefficient] = False
		coefficient += 1
	while p < 2000000:
		p += 1
		if boolNum[p]:
			sum += p
			print sum
			break

print ("hi")
print (sum)
