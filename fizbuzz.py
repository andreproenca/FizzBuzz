#  fizzbuzz: divisible for 3 and 5, fizz: divisible for 3, buzz: divisible for 5

from random import randint


def fizzbuzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    if n % 5 == 0:
        return 'buzz'
    if n % 3 == 0:
        return 'fizz'
    return n


for i in range(100):
    numRandom = randint(0, 100)
    print(fizzbuzz(numRandom))
