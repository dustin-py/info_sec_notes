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

## **sed**
> A powerful and complex stream editor. At a very high level, `sed` performs text exiting on a stream of text, either a set of specific files or standard output.

- **EX:**
    Here is a small example of its use:
    We will `echo`(output) a `string of text` then `|`(pipe) the text into `sed` and edit the text to be returned.

        user@domain:~$ echo "string of text" | sed 's/text/words/'

## **cut**
> The `cut` command is simple, but often comes on quite handy. It is used to extract a section of text from a line and output it to the standard output. Some of the most commonly-used switches include `-f` for the field number we are cutting and `-d` for the field delimiter.

- **EX:**
    `echo`(print) "some text, seperated, by stuff, ya" `|`(pipe) the output to `cut` `-f` feild number `-d` delimiter ","

        user@domain:~$ echo "some text, seperated, by stuff, ya" | cut -f 2 -d ","

## **awk**
> `awk` is a programming language designed for text processing and is typically used as a data extraction and reporting tool. It is also extremely powerful and can be quite comple. Commonly used switch is `-F`, which is the field separator and the print command, which outputs the result text.