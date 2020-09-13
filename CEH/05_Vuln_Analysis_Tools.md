# **Vulnerability Analysis Tools**
Tools used for vulnerability assessments.

---
## **Types of Vuln Assessments**
1. **Product Based:**
    - Installs on clients system.
    - Inside network
    - ***internal***

2. **Service Based:**
    - Cloud based services
    - third party
    - ***external***
---
## **Tool Types**
1. **Tree Based:**
    - Scans are tailored towards what is being scanned by the information thats given.
    - What that means is like; is this a web service, os type, what specificly do you want to scan.
    - use when you know exactly what to scan.

1. **Infrence Based:**
    - looks at the system that you wish to scan and kinda gets an idea of what is going on within it an tailors its assessment towards that.
    - infers from what it sees telling what types of scans should be done.
    - use when you are unsure of what to scan.

1. **Host Based:**
    - checking Oporating Systems for flaws

1. **Depth Assessment:**
    - these tools are basically fuzzers.
    - they find previously unknown vulnerabilities.
    - helps look for zero-days

1. **Application Layer:**
    - scans for web apps, software apps, data bases, etc..
    - looking for known vulnurabilities. 

1. **Active Scanners**
    - activly prob for information

1. **Passive Scanners**
    - grab already available information

1. **Scope Tools**
    - covers the range of the scopes engagement
---
## **Tools**
- **GFILanguard** --gui

- **`nikto`** --cli
    - for web apps vuln scans
    - use for reporting output

- **`wpscan`** --cli
    - scans wordpress sites

- **`nesus`** --gui *very expensive*

- **`openvas`** --gui 
    - highly informative gui scanner
    - knock off nesus
    - **Coommon Vulnerability Scoring System**
        - *CVSS*
        - **AV:N/AC:H/Au:N/C:C/I:C/A:CL**
            - **AV**: Attack Vector
            - **AC**: Attack Complexity
            - **Au**: Authentication
            - **C**: Confidentiality
            - **I**: Integrity
            - **A**: Availability
    
    - **CVSS V3 Scores**
        - **None**: 0.0
        - **Low**: 0.1-3.9
        - **Medium**: 4.0-6.9
        - **High**: 7.0-8.9
        - **Critical**: 9.0-10.0 