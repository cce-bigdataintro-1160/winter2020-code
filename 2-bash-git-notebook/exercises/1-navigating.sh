Find out what’s your username. Find your home directory and list its contents.
➜  ~ whoami
elomonaco

Change directory to / and list the contents of this directory. Why is this a special directory?
➜  ~ cd /
➜  /

Change directory to /var/log and list its files. What do we have here?
➜  / cd /var/log
➜  log ls -l
total 1516
-rw-r--r--  1 root              root                 0 Jan 22 20:40 alternatives.log
-rw-r--r--  1 root              root             11505 Jan 12 16:53 alternatives.log.1
-rw-r--r--  1 root              root               161 Mar 25  2019 alternatives.log.2.gz
-rw-r--r--  1 root              root              3927 Mar 12  2019 alternatives.log.3.gz
This contains all logs!

From the previous dir /var/log type cd ~, check your new directory using pwd.
➜  log cd ~
➜  ~ ls -l
total 660
-rw-r--r-- 1 elomonaco elomonaco     33 Jan 12 17:13 aaa
This is the home Dir!

Test the following commands: cd ., cd .., cd / and cd ~. Can you explain what each of those symbols mean?
cd . => Navigate to same dir(does nothing)
cd .. => Navigate to previous directory
cd / => Navigate to root
cd ~ => Navigate to home

From your home directory test both commands and explain the difference: cd Desktop and cd /Desktop
cd Desktop navigates to Desktop inside my home dir
cd /Desktop tries to go to Desktop from root, which doesn't exist
➜  ~ cd /Desktop
cd: no such file or directory: /Desktop

What command can give you the most recently modified file in your home directory? Hint, use man ls to find the right flags to use.
➜  ~ ls -ltr
total 660
-rw-r--r-- 1 elomonaco elomonaco   8980 Feb  9  2019 examples.desktop

Download the file titanic.zip and locate it through the shell by navigating and listing it. Tip: it will be in your Downloads directory, inside the your home directory.
➜  ~ cd ~/Downloads
➜  Downloads unzip titanic.zip
Archive:  titanic.zip