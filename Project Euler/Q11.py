def triNum (num):

    total = 0

    while num > 0:

        total += num

        num -= 1

    return total

def giveNumDiv (num):

    numDiv = 2

    for div in range (2, int(num**0.5 + 1)):

        if num % div == 0:

            numDiv += 2

    return numDiv

curNum = 2160

while True:#giveNumDiv(triNum(curNum)) <= 500:

    if giveNumDiv(triNum(curNum)) >50:

        print curNum, triNum(curNum), giveNumDiv(triNum(curNum))

    curNum += 1

print curNum