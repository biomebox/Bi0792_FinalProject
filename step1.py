#!/usr/bin/env python3

#step1 by Chandra Sarkar
### Replacing all the "-" characters in the alignments

######### Importing required modules #########
import sys
import os
##############################################

######### Setting up arguments and filenames and Initializing the script #############
input_file_path = os.path.join(sys.argv[1])     # Read in the first argument from the bash wrapper
in_file = open(input_file_path,'r')             # Open the file for reading

filename = os.path.basename(input_file_path)    # Get the filename
filename = filename.strip("outputcds")          # Modify the filename: Get rid of preceding term "outputcds" 
filename = filename.strip(".fas")               # Modify filename: Get rid of .fas extension

output_folder_path = os.path.join(sys.argv[2],filename+'.txt') # Read in the second argument from the bash wrapper and name the output file
out_file = open(output_folder_path, 'w')        # Open the file for writing

hdr_ct=0
#######################################################################################

################# Main loop #################
for line in in_file:                     # For each line in the file
        if line.startswith('>'):         # If the line is a header line, then do:
            hdr = line                   # Set header line apart
            hdr_ct += 1                  # Count no. of headers as a check if required
            out_file.write("%s"%hdr)        # Formatting and writing the header to output file

        else :                              # Else if the line is a sequence line,
            seq = line.replace("-","")      # Replace the "-" with nothing
            out_file.write("%s"%seq)        # Write the formatted sequence to outputfile
            
##############################################
        
in_file.close()     # closing input file
out_file.close()    # closing output file


#print("python",output_folder_path, hdr_ct)    # use this print as a checkpoint if required        
           

