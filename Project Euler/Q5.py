import math

numbers = []

 

def gcd (a, b):

    if (b == 0):

        return a

    return gcd (b, a % b)

 

def LCM (a,b):

    return a*b/gcd (a,b)

   

def LCM_list(list):

    return reduce(LCM, list)

   

for x in range (2,21):

    numbers.append (x)

 

number = LCM_list (numbers)

 

print (number)

