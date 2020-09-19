# **The Hacker Mentality and Tips**
---
- SCAN BABY SCAN
- if smbclient is throwing `ERROR: client min protocol = NT1`:
    1. Open configuration file in editor by typing `sudo nano /etc/samba/smd.conf`
    1. Add `client min protocol = NT1` to the `[Global]` section, anywhere is fine.
- enum4linux may not always work, use metaspoit instead maybe
- msf auxiliry modules pre-exploities
- msf exploiting best practice `show targets`
- if able to get a meterpreter shell always run `getuid` to check privillage level
- also in meterpreter make note of `getsystem` and `hashdump`
- in meterpreter type `shell` to gain shell access to target
- **Scanning methods**
    - keep it simple stupid `nmap -A -T4 -p- <target>`
    - need for speed and only need to know open ports `nmap -T4 <target>` only see the top 1000 without `-p-`
- **masscan stuff**
    - faster than nmap, but a little more messy
- buffer overflow attack against service version
- Ask yourself, why is anonymous login allowed!?
- if file is on server we need to get someone to maybe execute it for me
- ssh is not what we are looking for when trying to run exploits, they are only vuln when it comes to Social Engineering(last resort brute force)
- in `/etc/passwd` does not have passwords, root is always at top and users are always at bottom
- actual password hashs are stored in `/etc/shadow`
- **tool**: `unshadow passwdfile shadowfile` gives full hash
- hashs:`$1$` md5
- if you see windows 7 smb think enternal blue
