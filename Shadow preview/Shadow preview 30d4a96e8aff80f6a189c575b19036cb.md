# Shadow preview

**About:**

- Category: Web
- Level: Medium

**Subject:**

Une équipe produit a déployé en urgence un nouveau module “URL Preview” pour améliorer l’expérience utilisateur. Depuis, des comportements étranges ont été observés dans les journaux d’accès, sans qu’aucune compromission évidente ne soit détectée. Votre mission : retrouver le secret laissé sur l’infrastructure. Flag format: CCOI26{...}

**Resources:**

- site url: [http://87.106.89.40:8080/](http://87.106.89.40:8080/)
- github: https://github.com/Darylabrador/CTF-Challs/tree/main/web/Shadow%20Preview

In this challenge , we are given the website and the source code of it in a github.

First, let’s see what is the site web is about

1. Enum

As for the folder structure we see 

![image.png](Shadow%20preview/image.png)

so by this we can say that we are in the presence of a dockerized  web app with nginx as intermediary. 

![image.png](Shadow%20preview/image%201.png)

For the stack used, we can see 

- node with express

![image.png](Shadow%20preview/image%202.png)

- flask with python

![image.png](Shadow%20preview/image%203.png)

For the node web app, it’s just serve the web app given in the challenge

![image.png](Shadow%20preview/image%204.png)

and from what we can see in the docker-compose yaml file

![image.png](Shadow%20preview/image%205.png)

we see that port is bind for the host in the file 

![image.png](Shadow%20preview/image%206.png)

For the flask web app instead, it exposes port but not for host network ; the port only work internally in the docker network

![image.png](Shadow%20preview/image%207.png)

1. Interpretation and hypothesis

so far what we have are:

- 2 Web app :
    - one serve the web page
    - and one serve internally the get /flag   api endpoint
    
    ![image.png](Shadow%20preview/image%208.png)
    

we have also the folder structure hint web and internal

so from these we can test the hypothesis of the SSRF vulnerability

https://portswigger.net/web-security/ssrf

![image.png](Shadow%20preview/image%209.png)

1. Test the SSRF

how can we craft a url that launches in the web app will fetch the /flag endpoint in the flask app

- test [localhost](http://localhost) but failed

![image.png](Shadow%20preview/image%2010.png)

- like it’s in docker, [localhost](http://localhost) not working because each service has each own name and an associated IP in the docker internal network so let’s try internal:9000

 

![image.png](Shadow%20preview/image%2011.png)

aah we can see in the web app this restriction 

![image.png](Shadow%20preview/image%2012.png)

so these address are blocked but in the entrypoint we can see that it is accessible from all interfaces 

![image.png](Shadow%20preview/image%2013.png)

- so for the test we ll use this hint [http://0.0.0.0:9000/flag](http://0.0.0.0:9000/flag) to bypass this SSRF filter and eureka we have the flag

![image.png](Shadow%20preview/image%2014.png)
