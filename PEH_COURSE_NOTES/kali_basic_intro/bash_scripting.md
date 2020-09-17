# **Bash Scripting Commands**
---
- **grep**
    - serch by regex pattern
- **cut**
    - allows for text parsing and slicing
- **tr** 
    - translate as in manipulate text
- **for loops**
    
        for <var> in <some range>; do
        <action to perform> &
        done

        for <var> $( cat file.txt ); do [action] & or ; done
        
- **if then statements**

        if [condition]
        then
        [action]
        else
        [action]
        fi 

- **Example Bash Script Ping Sweep**

        #!/bin/bash

        if [ "$1" == "" ]
        then
        echo "You forgot an ip address!"
        echo "Syntax: ./ipsweep.sh 192.168.1*

        else
        for ip in 'seq 1..254'; do
        ping -c 1 $1.$ip | grep "64 bytes" | \
        cut -d " " -f 4 | tr -d ":" &
        done
        fi
