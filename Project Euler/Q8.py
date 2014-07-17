product = 1

bigProduct = 0

index = 0

 

number = input ("Please enter input:")

sequence = ""

 

assert (len(str(number)) > 12)

 

for i in range (0, len(str(number)) - 12):

    for x in range (i, i + 13):

        product *= int(str(number)[x])

 

    print ("Product: {0}".format (product))

   

    if (product > bigProduct):

        bigProduct = product

        index = i

    product = 1

 

for x in range (0,13):

    sequence += str(number)[index + x]

   

print "The sequence {0} produces the greatest product of {1}.".format (sequence, bigProduct)

 

#Alternate:

 

# for i in range(0, 1000) :

#     sub = s[i:i+13]

#     v = 1

#     for n in sub :

#         v *= int(n)

       

#     if v > m :

#         m = v

       

# print m