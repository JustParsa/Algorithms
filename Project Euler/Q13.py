fin = open ("num.txt", 'r')

sum = 0

for line in fin:
     sum += int (line)

while sum > 10000000000:
     sum /= sum

print (sum)