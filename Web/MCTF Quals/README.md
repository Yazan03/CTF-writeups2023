# Writeup for  Meat graphs from MCTF Quals 
<p align="center">
  
<img src="https://github.com/Yazan03/CTF-writeups/assets/94278827/ec394e9e-243c-4048-836f-2c89e4830289" />

</p>

![Screenshot 2023-11-12 063346](https://github.com/Yazan03/CTF-writeups/assets/94278827/01b54c4a-7731-414d-83bc-56ad2ca4f6c3)

```Introduction:```

It was a static web page then i started exploring. Armed with Burp Suite, my journey began with intercepting requests, uncovering a GraphQL endpoint within two requests. The second, more intriguing one, became the focal point of my exploration.

![Screenshot 2023-11-12 064525](https://github.com/Yazan03/CTF-writeups/assets/94278827/c3009d71-f9e1-460f-9e77-eb30786d7285)

```Enumeration```

Executing an introspection query, it return data back.

![Screenshot 2023-11-12 064620](https://github.com/Yazan03/CTF-writeups/assets/94278827/2b09051f-003f-43c6-869e-6ee0b6e7d46a)

Visualizing it through GraphQL Voyager shed light on the crucial "products" table, which, exposed a test connected to another table with filename and description.

![image](https://github.com/Yazan03/CTF-writeups/assets/94278827/233f4945-6a5c-4821-9b9e-df7f4918056f)

```Exploitation```

Then i craft a query to test if i can return values of price, name and id and it worked !, I noticed a filename associated with the test. Initiating a subquery within the filename light up and idea. Considering the possibility of path traversal, I satrted enumerating the system. Surprisingly, attempts to read files returned a status code of 200, but with an error in filename and they added hint that the flag in ```/srv/flag.txt``` so it made sense.

![Screenshot 2023-11-12 064904](https://github.com/Yazan03/CTF-writeups/assets/94278827/bfe7ece5-e72a-49e2-a340-475d15ff2dfa)

Recognizing there is an input validation on the filename, Then i tried every technique i know and it all failed then i start thinking why we put such this ```....//``` to bypass the validation because maybe the website filter ```../``` into an empty string then i tried to add more ```......///``` and it worked !

![Screenshot 2023-11-12 065052](https://github.com/Yazan03/CTF-writeups/assets/94278827/f222a5f8-668e-4ad1-8611-59e2e7a1ed88)

At the end we Secured a top 10 place with my team ```L3ak``` and i got a 3rd blood on this challenge and the challenge maintained with only three solves.

<p align="center">
  
<img src="https://github.com/Yazan03/CTF-writeups/assets/94278827/7740d1cd-78fc-41f3-830f-2516ef110d35" />

</p>

![Screenshot 2023-11-12 130930](https://github.com/Yazan03/CTF-writeups/assets/94278827/0d4ff5c5-6f55-4b1d-aef9-e3ee976eca66)

