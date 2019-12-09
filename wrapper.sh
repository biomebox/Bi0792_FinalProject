#!/usr/bin/bash

# bash wrapper by Chandra Sarkar
### Function: -Runs a series of python scripts sequentially within a pipeline
###           -The files in the output folder of the previous script in sequence is the input for the next script
###           -Can be customized to start a pipeline in the middle steps of the pipeline


###################################################################
###############         USER INPUT SECTION          ###############
###################################################################

printf "\nThe directories in the current folder are:\n\n"   
ls -1l                                          # Prints the contents of current folder for user convenience.

printf "\nWhat is the starting directory? "     # Asks which directory should it start with.
read dir                                        # Reads user input for the starting point.

printf "\nWhich step do you want to start off with? "   # Corresponding to the starting directory, which
read start                                              # step should it start with. And takes the user input.

printf "\nWhich step do you want to end with? "         # Corresponding to the starting directory, how many
read stop                                               # steps does the useer want to do. And takes the user input.

### In case of starting from the middle steps ###

if [ $start -gt 1 ]         # If the starting 
then
    start=$((start+1))
fi

###################################################################
###############             MAIN SECTION            ###############
###################################################################

for i in $(seq $start $stop)                    # Starts a loop for the steps needed to be done
do
    ctr=0                                       # Counter for no. of files being processed
    mkdir -p step$i                             # Makes a directory if it does not exists.Else overwrites files in existing directory.
    

    for file in $dir/*                          # For each file in the directory
    do
        let ctr++                               # Increase counter by 1
        python3 step$i*.py $file step$i         # Call the python script for the associated step
    done
    
    sleep 0.40                                  # Resting period between each loop.
    printf "step $i: $ctr files processed\n";   # Print on screen information about each step.
    dir=step$i                                  # Set the input directory as the next consecutive directory.

done

