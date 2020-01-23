#!/bin/bash

# This sample script allows the user to provide a path
# The script then adds all files and lenght of files in the file_lenghts.txt file
# Finally our script prints the name of the file with the longest size in lines

PROVIDED_PATH=$1

rm -f /tmp/file_lenghts.txt

printf "Listing all files in ${PROVIDED_PATH} \n\n"
for f in $PROVIDED_PATH/*
do
  echo $f
  wc -l $f >> /tmp/file_lenghts.txt
done

LONGEST_FILE=$(sort -nr /tmp/file_lenghts.txt | head -n1)

printf "\nThe longest file is $LONGEST_FILE"