sum_of_squares = 0

square_of_sums = 0

 

for x in range (1,101):

    sum_of_squares += x**2

    square_of_sums += x

square_of_sums **= 2

 

print abs (sum_of_squares - square_of_sums)

