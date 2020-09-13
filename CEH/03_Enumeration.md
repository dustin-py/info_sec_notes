# **Enumeration**
---
## **What is enumeration?**
- Enumeration is activly gaining deatails about your target.
- ***Example:***
    - What OS is the target running
    - What software and versions are being used
    - User and Groups
    - What services are being ran
    - Networks being shared
    - Ports and thier status
    - etc...

- Usually done with scanning tools such as `nmap`

- **Specific services to target:**
    - `net bios`
    - `snmp`
    - `ldap`
    - `ntp`
    - `smtp`
    - `dns`
    - `voip`
    - `sip`

## **Get to Scanning**
---
### **S**.*imple*  **N**.*etwork*  **M**.*anagment*  **P**.*rotocol*
- widely used protocol
- tells us cpu, mem, disk utilization stats
- older versions have no encryption
- come in the form of a **M**.*anagment*  **I**.*information*  **B**.*ase* which uses obj identifiers (pointers)
- ***Example Code for Scan***

        user@host:~$ snmp-check <ip address>
        ## Returns alot of info to parse through

### **S**.*imple*  **M**.*ail*  **T**.*ransfer*  **P**.*rotocol* 
- good for verifying user accounts
- for this we use `telnet`
- standard smtp port is `port 25`
- **`telnet` commands**    
    - `VRFY <user@host>` verify credentials
    - `EXPN <user@host>` *extended info of credentials* 
    - `MAIL FROM:` send mail from a user
    - `RCPT TO:` send mail to user

### **Extra Stuff**
- **`finger`**: shows users logged into the network



---
## **Tools**
- `snmp-check` --cli
- `enum4linux1` *performs all standard enumerations* --cli
- `telnet` --cli