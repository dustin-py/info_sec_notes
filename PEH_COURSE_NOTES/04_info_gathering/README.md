# **Information Gathering**
---
## **Identify Target**
- `bugcrowd.com` to pick target
- look up items on websites regarding to breach credentials
- `hunter.io`
- we want to maybe get a valid list of names
- `theHarvester`
---
## **Gathering breached creds with breach-parse**
- github.com/hmaverickadams/breach-parse
- large file of cred dumps
- `./breach-parse.sh @foobar.com foobar.txt`
---
## **Web-Info Gathering**
---
- ### **Finding Subdomains**
    - need to id what subdomains are outthere
    - map the directories of the domain
    - `apt install sublist3r`  <- *search for subdomains*
    - `crt.sh` <- *uses certificate finger pirnting to aquire results, (website)*
    - google:`owasp amass` <- *takes a very long time*

- ### **Web Foundation**
    - `builtwith.com` <- *explains the tech the web app is running.*
    - google: `wappalyzer` <- *similar to builtwith*
    - `whatweb <url>` <- *cli similar to the above tools*

- ### **Analyze Web Traffic**
    - `burpsuit` <- gui app to monitor and manipulate web traffic
    -*Follow Setup Steps*
        - firefox favs
            - preferences
                - settings
                    - manual proxy config 127.0.0.1 8080
                    - got to firefox get CA
                    - back to burpsuit
                    - add firefox CA to burpsuit
---
## **Google Fu**
- very important to be good at google
- # google: `google search syntax`
- `site: <url> < -keywords to remove> filetype: <filetype>`
---
## **Social Media**
- use seperate account from real ones when performing recon
- people are the weakest point of security
