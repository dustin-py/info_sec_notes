# **Piping and Redirection**
> Every program run from the command line has three data streams connected to it that serve as communication channels with the external environment. View in table below:


|Stream Name|Description|
|---|---|
|Standard Input (STDIN)| Data fed into the program|
|Standard Output (STDOUT)| Output from the program (defaults to terminal)|
|Standard Error (STDERR)|Error messages (defaults to terminal)|


|Type|Oporator|
|---|---|
|PIPING| `\|` |
|REDIRECTION| `>`, `>>`, `<`|

## **Redirecting to a New File**
> This is convenient most of the time, but we can use the `>` operator to save the output to a file to keep it for future reference or manipulation.

- **EX:**
    Create a new file and store some text in it.

        user@domain:~$ echo "some text" > test.txt

    If we view `test.txt` it'll display `"some text"`

        user@domain:~$ cat test.txt
        some text

## **Redirecting to an Existing File**
> To append additional data to an existing file (as opposed to overwriting the file) use the `>>`operator

- **EX:**
    Add more text to an existing file from above.

        user@domain:~$ echo "more text" >> test.txt

    We use `>>` because `>` would overwrite the file.

    If we view `test.txt` it'll display all content.

        user@domain:~$ cat test.txt
        some text
        more text

## **Redirecting from a File**
> As you may have guessed, we can use the `<` operator to send data the "other way".

- **EX:**
    Lets pass the `test.txt` file into a program

        user@domain:~$ wc -m < test.txt
        18 <-- count of characters in file

## **Redirecting STDERR**
> According to th POSIX spec, the file descriptors for STDIN, STDOUT, and STDERR are defined as 0, 1, and 2 respactively. These numbers are important as they can be used to manipulate the corresponding data streams from the command line while executing or joining different commands together.

## **Piping**
> Piping is when you redirect the output of one command to the input of another command.