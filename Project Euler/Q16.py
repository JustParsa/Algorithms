number = input ("Please Enter a number whose digits you want to sum up:")

sum = 0

 

while (number != 0):

    sum += (number % 10)

    number /= 10

    print number

   

print sum