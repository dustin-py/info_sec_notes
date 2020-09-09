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
|REDIRECTION| `>` and `<`|

## **Redirecting to a New File**
> This is convenient most of the time, but we can use the `>` operator to save the output to a file to keep it for future reference or manipulation.

- **EX:**

        user@domain:~$ echo "some text" > test.txt

    If we view `test.txt` ill display `"some text"`

        user@domain:~$ cat test.txt
        some text

