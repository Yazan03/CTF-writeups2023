# Writeup for  Meat graphs from MCTF Quals 
<p align="center">
  
<img src="https://github.com/Yazan03/CTF-writeups/assets/94278827/ec394e9e-243c-4048-836f-2c89e4830289" />

</p>

![Screenshot 2024-01-04 152929](https://github.com/Yazan03/xss/assets/94278827/ab292890-e317-40f9-a16b-9c996c49e88f)

```Introduction:```

It was a static web page, then I started exploring. Armed with Burp Suite, my journey began with intercepting requests and uncovering a GraphQL endpoint within two requests. The second, more intriguing one, became the focal point of my exploration.

![Screenshot 2024-01-04 153013](https://github.com/Yazan03/xss/assets/94278827/8311f3e4-e361-4db2-adeb-d3efe86acd12)

```Enumeration```

Executing an introspection query, it return data back.



Visualizing it through GraphQL Voyager shed light on the crucial "products" table, which exposed a test connected to another table with a filename and description.

![image](https://github.com/Yazan03/xss/assets/94278827/251e505f-8521-40e3-b726-1867cfcf71ba)

```Exploitation```

Then I crafted a query to test if I could return values of price, name, and ID, and it worked !, I noticed a filename associated with the test. Initiating a subquery within the filename lights up an idea. Considering the possibility of path traversal, I started enumerating the system. Surprisingly, attempts to read files returned a status code of 200, but with an error in filename, and they added a hint that the flag in ```/srv/flag.txt``` made sense.

![Screenshot 2024-01-04 154134](https://github.com/Yazan03/xss/assets/94278827/6a69964e-81a0-4cfa-b673-2a72fccd1ecc)


Recognizing there is an input validation on the filename, I tried every technique I knew and it all failed. Then I start thinking about why we put this ```....//``` to bypass the validation because maybe the website filters ```../``` into an empty string. Then I tried to add more ```......///``` and it worked!

![Screenshot 2024-01-04 153111](https://github.com/Yazan03/xss/assets/94278827/ccd4029b-63bb-48d6-89ad-3dfd1182033c)

At the end, we secured a top-10 place with my team, ```L3ak```, and I got 3rd blood on this challenge, which was maintained with only three solves.

<p align="center">
  
<img src="https://github.com/Yazan03/CTF-writeups/assets/94278827/7740d1cd-78fc-41f3-830f-2516ef110d35" />

</p>

