1- Unzip (using the terminal) our titanic.zip,
unzip titanic.zip

2- Provide the shape/dimensions of the file train.csv?
Lines: wc train.csv
Headers: head -n2 train.csv

3- List the first 5 rows of the file. Now list the last 5.
head -n5 train.csv
tail -n5 train.csv

4- Print only the lines 3 to 5 of the file?
head -n5 train.csv | tail -n3

5- Print this file last 5 lines save the output to train_tail.csv
tail -n5 train.csv >> train_tail.csv

6- Fetch the file remorquages.csv from the API as in our examples.
curl http://donnees.ville.montreal.qc.ca/dataset/1d785ef8-f883-47b5-bac5-dce1cdddb1b0/resource/e62322fb-3e14-4ee0-b724-a77190dac8e7/download/remorquages.csv > file.csv

7- Can you explain the command grep John remorquages.csv | wc -l and why would you use it?
Count how many `John` occurence I have in my file

8- Split the train.csv file in multiple files with 20 lines each.
split -l20 train.csv