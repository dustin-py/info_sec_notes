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
## **Impotant Ports**
- **80, 443**: commonly found with exploits 
    - Type/s: HTTP, HTTPS 
- **139, 445**: commonly found with exploits
    - Type/s: samba 
- **22**: commonly strong not normal to attack
    - Type/s: ssh <- *secure shell*
## **Vuln Scans**
- dir enums and vuln scans
- `nikto`
