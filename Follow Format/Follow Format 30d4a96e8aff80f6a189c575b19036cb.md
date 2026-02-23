# Follow Format

**About:**

- Forensic challenge
- Level: Easy

**Subject:**

Our client sent us this image and told us that they deleted a file. Please help them recover it. The file contains confidential information. Flag format: CCOI26{S0mething_here} [https://cdn.cattheflag.org/cybercup/challenge1/challenge.img](https://cdn.cattheflag.org/cybercup/challenge1/challenge.img)

In this challenge, 

we are given a disk image

![image.png](Follow%20Format/image.png)

and like the subject says maybe we follow the format  and mount it  to analyze or maybe not 😏

But first let’s run our basic check:

- verify the real type

![image.png](Follow%20Format/image%201.png)

- then metadata check

![image.png](Follow%20Format/image%202.png)

no thing interesting also there

- but maybe strings like let ‘s try

![image.png](Follow%20Format/image%203.png)

eureka we found our flag ( *never thought i would be this easy* 😏)

![image.png](Follow%20Format/image%204.png)