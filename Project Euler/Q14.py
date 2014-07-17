chain = 1

large_chain = 0

large_chain_number = 0

it_number = 2

while it_number < 1000000:

    number = it_number

    while number != 1:

        if number % 2 != 0:

            number = number * 3 + 1

            chain += 1

        if number % 2 == 0:

            number /= 2

            chain += 1

        if large_chain < chain:

            large_chain = chain

            large_chain_number = it_number

    it_number += 1

    chain = 1

print large_chain_number, large_chain