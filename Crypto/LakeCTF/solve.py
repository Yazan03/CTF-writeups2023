from mt19937predictor import MT19937Predictor
from Crypto.Util.number import *
f=open("s.txt").readlines()
a=[int(i.strip()) for i in f]
predictor = MT19937Predictor()
counter = 1
for x in range(624):
    predictor.setrandbits(a[988-624+x], 1024)

p=predictor.getrandbits(1024)
while True:
    q=predictor.getrandbits(1024)
    if isPrime(q):
        break
n=p*q
phi=(q-1)*(p-1)
e=65537
c=...
d=inverse(e,phi)

print(long_to_bytes(pow(c,d,n)))
