# Persistence Hunter

About:

- Forensic challenge
- Level: Easy

Subject:

Incident Response detected a suspicious PowerShell process spawning on a workstation at startup. We have managed to pull the users Registry hive find the persistence mechanism and decode the payload to reveal the flag. [https://cdn.cattheflag.org/cybercup/NTUSER/challengefile.DAT](https://cdn.cattheflag.org/cybercup/NTUSER/challengefile.DAT) CCOI26{S0mething_here}

Enum

![image.png](Persistence%20Hunter/image.png)

The file that is given is a Windows Registry file

since we can’t directly the flag

![image.png](Persistence%20Hunter/image%201.png)

Hypothesis: We need to investigate this windows registry 

For so i use regripper on linux,

![image.png](Persistence%20Hunter/image%202.png)

so, then we use reggriper with the hive type/profile ntuser like specify by the subject

![image.png](Persistence%20Hunter/image%203.png)

still no direct flag

![image.png](Persistence%20Hunter/image%204.png)

then we try to analyse the  “*Incident Response detected a suspicious PowerShell process spawning on a workstation at startup”* from the subject and instead search for powershell execution

regripper -r challengefile.DAT -f ntuser | grep powershell

and then we see an interesting base64 text with powershell

![image.png](Persistence%20Hunter/image%205.png)

decrypt it then voila, we got our flag

![image.png](Persistence%20Hunter/image%206.png)