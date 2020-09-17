# **Useful Commands**
---
## **Network Commands**
- **ping**
    - ICMP Request: another word for ping
    - `ping <ip>`: ping ip address.
    - `ping -c <num> <ip address>`: set amount of pings.

- **arp**
    - `arp -a`
    - shows ip address it talks to and the mac address it belongs to.
    - associate ip to mac

- **netstat**
    - `netstat -ano`
    - active connections running on each machine

- **route**
    - returns routing table
---
## **Editor**
- `nano`: terminal text editor
- `gedit`: gui text editor
---
## **Services**
- **Apache2**
    - web server
    - `service apache2 start`: starts apache web server
- **python web server**
    - `python -m SimpleHTTPServer port 80 or 443 or 8080`
- **python ftp server**
    - `python3 -m twisted ftp1`
- **systemctl**
    - used to enable and diasable services for boot
    - `systemctl enable or disable <service>`
- **postgresql**
    - start at boot for use with meta sploit
    - `systemctl enable postgresql`
---