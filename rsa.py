from math import sqrt
import random

p = 7
q = 11

def getPrimesList(to):
    res = []
    for i in range(2, to):
        t = int(sqrt(i) + 1)
        for j in res:
            if j > t:
                res.append(i)
                break
            if i % j == 0:
                break
        else:
            res.append(i)
    return res

def removeDividers(value, primes):
    res = []
    for prime in primes:
        if value % prime != 0:
            res.append(prime)
    return res

def findD(fi, e): 
    # (d * e) % fi == 1
    d = 2
    while True:
        if (d * e) % fi == 1:
            return d
        d += 1

def cryptString(msg, key):
    res = ''
    for char in msg:
        res += cryptChar(char, key)
    return res

def cryptNum(msg, key):
    return (msg ** key[0]) % key[1]

def cryptChar (char, key):
    acode = ord('A')
    return chr(((ord(char) - acode) ** key[0]) % key[1] + acode) # прибавляем-вычитаем код А из-за проблем с маленьким вторым значением ключа (key[1] = 77, а код шифруемого символа 82)

def printStringCodes(val):
    print(' '.join(map(lambda x: str(ord(x)), val)))

def main():
    n = p * q
    fi = (p-1)*(q-1)
    primes = getPrimesList(fi)
    filteredPrimes = removeDividers(fi, primes)
    e = filteredPrimes[random.randrange(len(filteredPrimes))]
    openKey = (e, n)
    d = findD(fi, e)
    secretKey = (d, n)
    data = 'CHAIR'
    print('to encrypt: ', data)
    #printStringCodes(data)
    encrypted = cryptString(data, openKey)
    print('encrypted: ', encrypted)
    #printStringCodes(encrypted)
    decrypted = cryptString(encrypted, secretKey)
    print('decrypted: ', decrypted)
    #printStringCodes(decrypted)
    print('p = ', p, ', q = ', q, ', n = ', n, ', fi(n) = ', fi, ', e = ', e, ', d = ', d)


if __name__ == '__main__':
    main()