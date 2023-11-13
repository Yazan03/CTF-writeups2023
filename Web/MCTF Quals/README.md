Writeup for  Meat graphs from MCTF Quals 

![Screenshot 2023-11-12 063032](https://github.com/Yazan03/CTF-writeups/assets/94278827/ec394e9e-243c-4048-836f-2c89e4830289)


![Screenshot 2023-11-12 063346](https://github.com/Yazan03/CTF-writeups/assets/94278827/01b54c4a-7731-414d-83bc-56ad2ca4f6c3)

```Introduction:```

It was a static web page beckoning exploration. Armed with Burp Suite, my journey began with intercepting requests, uncovering a GraphQL endpoint within two requests. The second, more intriguing one, became the focal point of my exploration.

![Screenshot 2023-11-12 064525](https://github.com/Yazan03/CTF-writeups/assets/94278827/c3009d71-f9e1-460f-9e77-eb30786d7285)

```Enumeration```

Executing an introspection query, I unearthed a trove of data.

![Screenshot 2023-11-12 064620](https://github.com/Yazan03/CTF-writeups/assets/94278827/2b09051f-003f-43c6-869e-6ee0b6e7d46a)

Visualizing it through GraphQL Voyager shed light on the crucial "products" table, which, intriguingly, led to a test connected to another table with filename and description.

![image](https://github.com/Yazan03/CTF-writeups/assets/94278827/233f4945-6a5c-4821-9b9e-df7f4918056f)

Then i craft a query to test if i can return values of price, name and id and it worked !, I noticed a filename associated with the test. Initiating a subquery within the filename opened a new avenue. Considering the possibility of path traversal, I embarked on enumerating the system. Surprisingly, attempts to read files returned a perplexing status code of 200, accompanied by an error-ridden filename and they added hint that the flag in /srv/flag.txt so it made sense.

![Screenshot 2023-11-12 064904](https://github.com/Yazan03/CTF-writeups/assets/94278827/bfe7ece5-e72a-49e2-a340-475d15ff2dfa)


