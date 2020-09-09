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
