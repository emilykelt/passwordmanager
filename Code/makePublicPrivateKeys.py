import random, primeNum, cryptomath


def generateKey(keySize):
    p = 0
    q = 0
    #prime numbers p and q, calculate p*q
    while p==q:
        p = primeNum.generateLargePrime(keySize)
        q = primeNum.generateLargePrime(keySize)
    n = p*q

    #generate e, relatively prime to (p-1)*(q-1)
    while True:
        e = random.randrange(2**(keySize-1), 2**keySize)
        if cryptomath.gcd(e, (p-1)*(q-1))==1:
            break
    
    #calculate d, mod inverse of e
    d = cryptomath.findModInverse(e,(p-1)*(q-1))

    publicKey = (n,e)
    privateKey = (n,d)
    #print(publicKey, privateKey)
    return publicKey,privateKey

#publicKey, privateKey = generateKey(1024)
