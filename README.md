# **Finding your way around kali:**
## **The Linux Filesystem**
> Kali Linux adheres to the filesystem hierarchy standard (FHS), which 
provides universal layout for all Linux users.

- **/bin** :basic programs (ls, cd, cat, etc..)
- **/sbin** :system programs (fdisk, mkfs, sysctl, etc..)
- **/etc** :configuration files.
- **/tmp** :temporary files (typically deleted on boot)
- **/usr/bin** :applications (apt, ncat, nmap, etc..)
- **/usr/share** :application support and data files.

## **RTFM (READ THE FUCKING MANUAL)**
**man:** access the manual of commands/programs
- **Ex Commands:**
    - **man -k <key_word>:** key word search man pages 
    
    - **Typical Manpage Format:**
    
|**Section**|**Contents**|
|---|---|
|1 |: User Commands|
|2 |: Programming interfaces for kernael system calls|
|3 |: Programming interfaces to the C library|
|4 |: Special files such as device nodes and drivers|
|5 |: File formats|
|6 |: Games and amusements such as screen-savers|
|7 |: Miscellaneous|
|8 |: System administation commands|

## **Finding Files in Kali Linux**
> Three of th most common Linux commands used to locate files in Kali
Linux include find, locate, and which. These utilities have similarities,
but work and return data in different ways and therefore may be useful in
different circumstances.

- **which** :searches through dirs found in the `$PATH` environment var
for a given file name.
- **locate** :quickest way to find the locations of files and dirs.
The shorter search time is made possible by searching built-in database 
named `locate.db` rather than the entire hard disk itself.
- **find** :most complex and flexible search tool among the three. RTFM

## **Setting Path**
> The `$PATH` is the environment to put dirs & files so that it 
executes by `name.file` instead of `~./this/dir/here/name.file`

- **Example of addind to path:**
	
		export PATH=$PATH:/place/with/the/file

# **Managing Kali Linux Services:**
> Kali is a specialized distro aimed at security professionals. Kali 
installation ships with several services preinstalled such as `SSH`, 
`HTTP`, `MySQL`, etc. Consequently, these services would load at
boot, which result in Kali exposing several open ports by default-something 
we want to avoid for security reasons. Kali deals with this issue by 
updating its settings to prevent network services from starting at boot.

> Kali also contains a mechanism to both whitelist and black list
various services.

## **SSH Service**
> Secure SHell service, commonly used to remotely access a computer,
using a secure, encrypted protocol. SSH service is TCP-based and 
listens by default on port 22.

- **Start SSH Service** :When this command completes successfully,
it does not return any output.

		sudo systemctl start ssh

- **Verify SSH Service** :run and listen on TCP port 22

		sudo ss -antlp | grep sshd

- **Start SSH Services on Boot** 
`systemctl` enables and disables most services within Kali

		sudo systemctl enable ssh 

## **HTTP Service**
> The Apache HTTP service is often used during a penetration test, 
either for hosting a site, or providing a platform for downloading files
to a victim machine. The HTTP service is TCP-based and listens defaulted
on port 80.

- **Start HTTP Service** 

		sudo systemctl start apache2

- **Verify HTTP Service**

		sudo ss -antlp | grep apache

- **Start HTTP Services on Boot**

		sudo systemctl enable apache2

## **View all Services**
> See a table of all available services

		systemctl list-unit-files


# **Searching, Installing, and Removing Tools:**
- **update**

		apt update  

- **upgrade**

		apt upgrade [optional <program_name>]

- **Search apt cache**

		apt-cache search <program_name>

- **Verify search results**

		apt show <program_name>

- **install**

		sudo apt install <program_name>

- **remove** 

		sudo apt remove --purge <program_name>

- **dpkg** :core tool used to install a package.

		sudo dpkg -i <pkg_name>
