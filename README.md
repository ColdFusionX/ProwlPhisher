# ProwlPhisher

## Automated Phishing Tool 

Script which I wrote using Python modules to send automated Phishing mails 

Intended only for educational and testing in corporate environments.

Script was tested on Python 3.8.6

### Usage:

```shell
cfx:  ~/ProwlPhisher
→ ./prowlphisher.py -h
usage: prowlphisher.py [-h] [-e EMAILS]

ProwlPhisher by ColdFusionX

optional arguments:
  -h, --help            show this help message and exit
  -e EMAILS, --emails EMAILS
                        Email Wordlist

Script Usage : 
./prowlphisher.py -e emails.txt
```

### Additional required Python modules :
- pwn

Installation:
```shell
pip3 install pwn
```

### Proof of Concept :

This script expects one user inputs :
- **Email List** - Emails Wordlist

#### Expected Outputs :

The script shall flag if incase the wordlist contains any invalid address which SMTP server fails to recognize thereafter unable to send mail:

```shell
cfx:  ~/Documents/htb/sneakymailer 
→ ./prowlphisher.py -e emails.txt 
[\] Sending Mail to -> colfx@auto.bots

[-] Error Sending mail to colfx@auto.bots

[+] Phising Mail Sent
```
Successful Output:

```shell
cfx:  ~/ProwlPhisher 
→ ./prowlphisher.py -e emails.txt 
[↗] Sending Mail to -> Optimusprime@auto.bots

[+] Phising Mail Sent
```
