def isPalindrome (number):

    strNum = str (number)[::-1]

    print "In reverse: ", strNum

    if (number == int(strNum)):

        return True

    return False

 

palindromes = []

 

for x in range (100, 1000):

    for y in range (100, 1000):

        if (isPalindrome (x*y) == True):

            palindromes.append(x*y)

 

palindromes.sort()

print (palindromes)

 

print (palindromes[len(palindromes)-1])