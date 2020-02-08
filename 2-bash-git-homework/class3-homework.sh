#!/bin/bash

# This for iterates 4 times over the items [0, 1, 2 and S].
for DIR in 0 1 2 S

# Do statement just starts the actions of the loop
do
    #For each item we create a directory in the current working path called <item>-files
    mkdir ${DIR}-files
    #Then we create an empty file inside this directory called <item>-files/<item>
    touch ${DIR}-files/$DIR

# Done statement finishes the loop, anything after this won't be repeated
done

