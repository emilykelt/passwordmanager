import math, random

#the functions return true if it is a prime number otherwise they return false
def isPrimeTrialDiv(num):
    if num<2:
        return False

#trial division algorithm for testing primality
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
        return True

#sieve of eratosthenes
def primeSieve(sieveSize):
    #creates blank array of however many numbers we want to find the primes up to, and sets the first two numbers 0 and 1 as false
    sieve = [True]*sieveSize
    sieve[0] = False
    sieve[1] = False

    #if > sqrt of sieveSize then the factors will be repeated so for efficiency we only go up to sqrt(sieveSize) + 1
    for i in range(2,int(math.sqrt(sieveSize))+1):
        pointer = i*2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i

    #from the boolean list it creates a list of their indexes
    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)

    return primes

def rabinMiller(num):
    if num % 2 == 0 or num <2:  
        return False

    #quick prime
    if num == 3:
        return True

    s = num -1
    t = 0

    #factors out powers of 2
    while s%2==0:
        s = s//2
        t+=1

    #test 5 times to check primality
    for trials in range(5):
        a = random.randrange(2,num-1)
        v = pow(a,s,num)
        if v != 1:
            i = 0
            while v != (num-1):
                if i == (t-1):
                    return False
                else:
                    i = i+1
                    v = (v**2) % num

    return True

lowPrimes = primeSieve(100)

def isPrime(num):
    #does a quick prime number check before calling rabinMiller
    if (num<2):
        return False
    for prime in lowPrimes:
        if (num%prime==0):
            return False
        
    return rabinMiller(num)

def generateLargePrime(keysize):
    while True:
        #generates random number within the range of the keysize
        num = random.randrange(2**(keysize-1), 2**(keysize))

        #makes sure the number is prime before returning, otherwise will keep looping
        if isPrime(num):
            return num
