Send to me in a private message:a.What this command do:
a. cat <file1> <file2> >> <file3>
Concatenates file1 and file2 into file3. If file3 doesn't exist, it gets created otherwise contents are appended to the end.

b.What this command do: cat <file> | head -n 3 | sort?
Prints 3 first lines of target file and sorts them alphabetically.

c.What does this command do:  find . -iname "*csv"
Find all csv files under the current directory, ignoring casing in the name.

a.What’s the command to list the most recently modified files in my current directory
ls -ltr

b.What’s the command to split a file into multiple 10 kilobytes files?
split -b 10k target_file

c.What’s the command to filter and print only the lines that contain the word “model” in the file “/proc/cpuinfo”?
grep model /proc/cpuinfo

d.What command would you use to remove all duplicated lines in a file? It’s ok to alter the original order of lines in the file.
cat target_file | sort | uniq