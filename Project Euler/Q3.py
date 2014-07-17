print ("This program will take a number and output all prime factors.")

number = input ("Please enter the desired number: ")

factors = []

div = 2

while (number != 1):

    while (number % div == 0):

        factors.append(div)

        number /= div

    div += 1   

print (factors)

