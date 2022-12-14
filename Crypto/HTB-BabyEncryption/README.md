We have the following code

```python
# CHALL.py

import string
from secret import MSG

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

ct = encryption(MSG)
f = open('./msg.enc','w')
f.write(ct.hex())
f.close()
```

Then we are given msg.enc
```msg.enc
6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921
````
Solution will be:
```python
import string
import codecs
f=open("msg.enc",'r')
enc_msg=f.read()
enc_msg_f=codecs.decode(enc_msg,'hex')
flag=""
for i in enc_msg_f:
    for j in range(32, 127):
        if((123 * j + 18) % 256)==i:
            flag+=chr(j)


print(flag)
```

```shell
❯ python solve.py
HTB{l00k_47_y0u_r3v3rs1ng_3qu4710n5_c0ngr475}
```
