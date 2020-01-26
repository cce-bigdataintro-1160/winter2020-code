Create a directory called learning-shell in your home directory
➜  mkdir ~/learning-shell

Copy it from your ~/Downloads directory into your learning-shell directory
➜  cp ~/Downloads/random_datasets.zip learning-shell

Unzip it using unzip random-datasets.zip
➜  unzip random_datasets.zip

Look at those files contents by printing some files in your directories using cat or less. What is the difference between the two?
Less opens file in interactive mode, cat dumps all content to console

Lets organize this by first moving all files that start with construction-spending into the directory construction-data
➜  mv construction-spending* construction-data

Rename Iris.csv into Iris_Classification.csv and move it into iris-species
➜  mv Iris.csv Iris_Classification.csv
➜  mv Iris_Classification.csv iris-species

Delete the delete-me directory.
➜ rm -r delete-me

Create a file (using nano or vi editors) called a_dataset.csv write a few lines in it and save it.
nano a_dataset.csv