In this challenge we have chall.py
```python
flag = b'yuctf{}'
key = b'********'
cipher = b''

for i in range(len(flag)):
        cipher+= chr(flag[i] ^ key[i%len(key)]).encode()
with open('cipher.enc' , 'wb') as f :
        f.write(cipher)

```
and cipher.enc
```
▒,_:CS:GC
```
the soltion : so we already know a part of flag if we xor it with the cipher we are going to have a part of the key
but it was't enough so i tried to bruteforce it, then we have it it's perfecto
```python
flag = open("cipher.enc",'rb').read()
key = b'perfecto'
pt = b''

for i in range(len(flag)):
        pt+= chr(flag[i] ^ key[i%len(key)]).encode()
print(pt)

```

```text
the flag yuctf{X0r_15_r3v3rsible}
```
