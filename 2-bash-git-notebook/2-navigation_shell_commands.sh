### Basic navigation shell commands

# date - Displays current date
date

# man - Displays the manual for all other commands in the shell
man date

# whoami - Print  the  user  name  associated  with the current effective user ID.
whoami

# pwd - Print the full filename of the current working directory.
pwd

# ls - List  information  about  the FILEs (the current directory by default).
ls                        # lists files in current directory
ls <directory_path>       # lists files in the target path
ls -l                     # lists in list format
ls -la                    # lists in list format including hidden files
ls -lt                    # lists in list format sorted by last modification date
ls -lr                    # lists in list format in reverse order

# cd - Changes current working directory using relative paths
cd <directory_path>   # navigages to target path
cd documents          # navigates to 'documents'
cd documents/cebd1160 # navigates to 'documents/cebd1160'
cd ~                  # navigates to /Users/<myusername> which is your Home directory where you have full access to all files
cd .                  # navigates to current working directory (does nothing)
cd ..                 # navigates to previous directory in hierarchy tree

# cd - Changes current working directory using absolute paths
cd /                  # navigates to root directory in hierarchy tree
cd /tmp               # navigates to /tmp directory using absolute path

# unzip - will list, test, or extract files from a  ZIP  archive
unzip <file_name>

# history - check all commands issued previously
history