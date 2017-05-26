# Find prime numbers until the user chooses to stop asking for the next one
# using generators

from math import sqrt


def isPrime(n):
    if n > 1:
        if n == 2 :
            return True
        if n % 2 == 0:
            return False
        for divisor in range(3,(sqrt(n)+1),2):
            if n % divisor == 0 :
                return false
            return True
        return False

def gen_prime():
    yield 2
    n = 2
    while(True):
        if isPrime(n):
            yield n
        n += 2

def main():
    print("Press enter to generate the next prime number, To stop press S")
    generator = gen_prime()
    while True:
        ans = raw_input()

        if ans == "s":
            break
        else:
            print generator.next()

if __name__ == '__main__':
    main()
