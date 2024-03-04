import random

def isPrime(num):   #uses the Rabin-Miller Primality Algorithm - not 100% accurate for primes
    # Returns True if num is a prime number.
    if num % 2 == 0 or num < 2:
        return False # Rabin-Miller doesn't work on even integers.
    if num == 3:
        return True
    s = num - 1
    t = 0
    while s % 2 == 0:
        # Keep halving s until it is odd (and use t
        # to count how many times we halve s):
        s = s // 2
        t += 1
    for trials in range(5): # Try to falsify num's primality 5 times.
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # This test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

def randomprime():
    
    primal = False
    number = 0

    while primal == False:
        number = random.randint(2,100)    #change max number depending on bits
        primal = isPrime(number)


    return number


def greatest_common_divisor(a, b):  #double check
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):      #double check
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a//m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(message, n, e):
    ciphertext = [pow(ord(char), e, n) for char in message]
    return ciphertext

def decrypt(message, n, d):
    for C in message:
        print(chr((C**d)%n)) #''.join([chr(mod_exp(char, d, n)) for char in message])   #TODO: THIS IS THE PROBLEM LINE, im getting the original values back, seems to do nothing? or encryp
    #return plaintext

def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0: 
        if exponent % 2 ==1:
            
            result = (result*base) % modulus
            exponent = exponent / 2
            base = (base * base)% modulus

        return result   #changed the tabs here
    

def rsa(message, to_encrypt):

    #generate two distinct primes p and q
    p = randomprime()
    q = randomprime()

    while q == p:           #makes sure they are unique primes
        q = randomprime()

    #compute N
    N = p * q # this is part of the public key

    #compute phi
    phi = (p-1)*(q-1)

    #choose any e between 1 and phi. making sure they are coprime
    e = random.randint(1,phi)
    while greatest_common_divisor(e, phi) != 1: #coprime means greatest common factor of both is one
        e = random.randint(1,phi)

    # find d 
    d = mod_inverse(e, phi)

    if to_encrypt == True:
        # encrypt message
        encrypted_message = encrypt(message, N, e)  #is an array
        return encrypted_message
    elif to_encrypt == False:
        decrypted_message = decrypt(message, N, d)
        return decrypted_message


message = 'hello'
encrypted_message = rsa(message,True)
print(encrypted_message)

decrypted_message = rsa(encrypted_message,False)
print(decrypted_message)

"""
TODO: fix decrypt function

does it encrypt correctly

"""
