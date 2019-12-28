### Gnu Core Tools utilitaries

# head - Print  the  first  10 lines of each FILE to standard output
head filename.txt
head -n5 filename.txt   # Prints 5 lines instead of 10

# tail - Print  the  last  10  lines of each FILE to standard output.
tail filename.txt
tail -n5 filename.txt   # Prints 5 lines instead of 10

# wc - Print the shape, newline, word, and byte counts for each FILE
wc filename.txt
wc -l file.txt          # Prints only the lines

# sort - sort or merge records (lines) of text
sort <file_name>

# head - Connecting commands using pipe
head -n5 file.txt | sort # Prints first 5 lines of file and sorts the result

# uniq - Filter  adjacent matching lines from INPUT
uniq filename.txt

# curl - curl is  a tool to transfer data from or to a server
  # See http://donnees.ville.montreal.qc.ca/dataset/remorquages-de-vehicules-genants
  # List all csv entries
  curl http://donnees.ville.montreal.qc.ca/dataset/1d785ef8-f883-47b5-bac5-dce1cdddb1b0/resource/e62322fb-3e14-4ee0-b724-a77190dac8e7/download/remorquages.csv
  # Saves output to a file called : remorquages.csv
  curl http://donnees.ville.montreal.qc.ca/dataset/1d785ef8-f883-47b5-bac5-dce1cdddb1b0/resource/e62322fb-3e14-4ee0-b724-a77190dac8e7/download/remorquages.csv > remorquages.csv

# > or >> - Outputting results to a file using > or >>
cat file1.txt > output.txt   # Always overwrites files
cat file1.txt >> output.txt  # Always appends to files

# display disk usage statistic
du -a .

# split - splits a file into multiple files of the size provided
split -l 10 train.csv

http://localhost:50070/explorer.html#/user
docker run -it -p 50070:50070 -p 50075:50075 sequenceiq/hadoop-docker:2.7.1 /etc/bootstrap.sh -bash
/usr/local/hadoop-2.7.1/bin/hdfs dfs -ls /
/usr/local/hadoop-2.7.1/bin/hdfs dfs -put