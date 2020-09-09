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

