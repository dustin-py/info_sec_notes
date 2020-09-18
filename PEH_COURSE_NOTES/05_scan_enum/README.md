# **Scanning and Enummeration**
- `arp-scan -l` <- what netdiscover is doing.
---
## **Nmap**
- tool for scanning networks and ports
- **Common Switches**
    - `-A`: scans for all such as; OS, versions, etc...
    - `-Pn`: ping scan
    - `-T4`: sets the intesity to 4, out of 6 levels
    - `sU`: udp port scan *takes a long time*
    - `sT`: full tcp port scan
    - `-O`: for OS detection *this is a guess*
    - `-p-`: scan all ports instead of just the top 1000
---
## **Impotant Ports**
- **80, 443**: commonly found with exploits 
    - Type/s: HTTP, HTTPS 
- **139, 445**: commonly found with exploits
    - Type/s: samba 
- **22**: commonly strong not normal to attack
    - Type/s: ssh <- *secure shell*
---
## **Vuln Scans**
- dir enums and vuln scans
- `nikto`: for dir enum and vuln scans
---
## **SMB Enum**
- smb is a fileshare
- `smbclient`: for accessing smb servers
---
## **SSH Enum**
- not common: `ssh <ip> -oKexAlgorithms=+diffie-hellman-group1-sha1`
- if no matching cipher found: `ssh <ip> -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes128-cbc`
- why attemp this connection?
    - sometimes it will return a banner even if denied
- ssh is a strong connection
---
## **Research Potential Vulnurabilities**
- google possible exploits for current versions target is running.
- `searchsploit`: tool to search exploit in command line *dont be specific*
---
