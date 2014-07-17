flag = False

 

import time

 

start = time.time()

 

for a in xrange (1, 1001):

    for b in xrange (a + 1, 1001):

        c = 1000 - b - a

        if (a**2 + b**2 == c**2):

                print "{0} + {1} + {2} = 1000.".format (a,b,c)

                print "a x b x c = {0}".format (a*b*c)

                flag = True

                break

    if (flag == True):

        break

        b += 1

    a += 1

print "Runtime: ", time.time() - start, "seconds\n"