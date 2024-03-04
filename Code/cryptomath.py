def gcd(a,b): #function takes two numbers a and b and finds the greatest common divisor using euclid's algorithm
    while a != 0:
        a,b = b%a, a
    return b

def findModInverse(a,m):    #returns mod inverse of a%m, the number x such that a*x % m = 1
    if gcd(a,m)!= 1:
        return None # no mod inverse
    #extended euclidian algorithm
    u1,u2,u3 = 1, 0, a
    v1,v2,v3 = 0, 1, m

    while v3 != 0:
        q = u3//v3
        v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3), v1, v2, v3 
    return u1 % m

#print(findModInverse(8953851,26))
