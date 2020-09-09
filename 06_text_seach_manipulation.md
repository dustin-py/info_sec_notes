# **Text Searching and Manipulation**
> Recommed looking up a bit about regular expressions for this part. The commands used for text searching rely on regular expressions.

## **grep**
> In a nutshell, `grep` searches text files for the occurrence of a given regular expression and outputs any line containing a match to the standard output, which is usually the terminal screen.

Common switches used are: `-r` for recursive searching and `-i` to ignore text case.

- **EX:**
    Here we will `ls`(list) all content in `/home/user` then `|`(pipe) `grep ^D`(search for everything that starts with `D`).

        user@domain:~$ ls /home/user | grep ^D
        Documents/
        Downloads/
        Desktop/ 

