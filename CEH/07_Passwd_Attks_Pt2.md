# **Password Attacks Part 2**
---
## **Befor the Fun**
- **Online Attacks**
    - attacking some sort of network authentication, ex; `telnet`, `ftp`, `ssh`, `http`, etc..

- **Offline Attacks**
    - we have the encrypted pass word hash and we attempt to crack the hash while offline.
---
## **Emplementation**
- **Online Attack Tools**
    - `medusa` --cli
    - `hydra` --cli
    - `ncrack` --cli
    - packet catching using `wireshark`

- **Offline Attack Tool**
    
    - `john` (john the ripper) hash cracker --cli
        - `john --show pass.list`
        - `~/.john/john.pot`
        - `john --format=UNIX`
    
    - `ophcrack` --gui
        - runs rainbow files. fancy stuffs look it up.
        - rtgen to create rt tables.

    - `rainbowcrack`
    
    - `hashcat` --cli
        - ***only use on a heavy duity machine***
        - lots of bells and whistles


# ***shadowfile***

# ***`memecats` & `fgdum` --gui Windows is special, in that it hides the shadow file when running. At start windows stores the shadow file in memory, so unlike linux where we can just `cat shadowfile`, in windows we have to find the hash in memory and piece it together.***  