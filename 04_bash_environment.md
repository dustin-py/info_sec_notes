# **The Bash Environment**
> Linux cmd line uses Bash Shell

When opening a terminal window, a new Bash process, which has its own
environment variable is initialized. These variables are a form of global storage for various settings inherited by any applications that are run during that terminal session. One of the most commonly-referenced environment variables is `PATH`, which is a colon-separated list of directory paths that Bash will search through whenever a command is run without a full path.

- **View PATH contents:**

        user@domain:~$ echo $PATH

- **Common Environment Variables:**
    - User Name
        
            user@domain:~$ echo $USER
    - Current Working Directory

            user@domain:~$ echo $PWD
    - Home Directory

            user@domain:~$ echo $HOME

- **Define Environment Variables:**
    - Define environment variables with `export` command.

            user@domain:~$ export var_name=<something_to_store> 

- **View all Environment Variables:**
    - output all global variables stored in the environment.

            user@domain:~$ env

