# **Additional Scanning Tools**
---
## **masscan**
- `masscan`: port scanning tool
- github: [masscan github](https://github.com/robertdavidgraham/masscan)
- built to scan the entire internet realy fast ***DONT DO THIS!!!!***
- Basic Scan: `masscan -p <port-range> <ip>
---
## **metasploit**
- `msfconsole`: command to start metasploit
    - `use 4`: command to use metasploits SYN scanner
        - `options`: this will show params/requirments
        - `set rhosts <target ip>`: set host to scan
	- `set ports 1-65535`: set port range
 	- `run`: run the scanner 
- `search`: search strings
---
## **Nessus**
- Vulnerability Scanner
- very useful tool to have and know
- google: nessus download from Tenable 64_Debian
    - open terminal: `dpkg -i <nessus download>`
    - follow nessus instructions that appear.
	- install nessus essential
	- will need email for activation code
- free edition allows the scan of any private ip address
- web gui
---
