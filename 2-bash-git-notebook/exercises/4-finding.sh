1- Find the person called Torborg in the titanic file train.csv
grep Torborg train.csv

2- Count how many people were male and female in the file
grep ",male" train.csv | wc -l
grep -w "male" train.csv | wc -l
grep "female" train.csv | wc -l

3- Count how many people called John are in the file and how many of them are male or female
grep "John" train.csv | grep female | wc -l
grep "John" train.csv | grep -w male | wc -l

4- Find all csv files in your home directory. Play with the -maxdepth flag to see the difference.
find ~ -maxdepth 2 -name "*.csv"

5- List all the grep commands you did today.
history | grep grep
