#!/usr/bin/env python3

#step2 by Chandra Sarkar
### to get rid of newline characters at the end of each line of the DNA sequence

######### Importing required modules #########
import sys
import os
##############################################

######### Setting up arguments and filenames and Initializing the script #############
input_file_path = os.path.join(sys.argv[1]) # Read in the first argument from the bash wrapper
in_file = open(input_file_path,'r')         # Open the file for reading

filename = os.path.basename(input_file_path)    # Get the filename
filename = filename.strip('.txt')               # Modify filename: Get rid of .fas extension

output_folder_path = os.path.join(sys.argv[2],filename+'.txt') # Read in the second argument from the bash wrapper and name the output file
out_file = open(output_folder_path, 'w')                       # Open the file for writing 

hdr_ct=0
#######################################################################################

for line in in_file:          # For each line in the file
        
    if line.startswith('>'):  # If the line is a header line, then do:
        hdr_ct += 1           # Count no. of headers as a check if required
        hdr = line            # Set header line apart
        #print(hdr)
        out_file.write("\n%s"%hdr)  # Formatting and writing the header to output file
            
    elif not line.startswith('>'):  # Else if the line is a sequence line,
        read_seq = str(line)        # Convert line object into a string -optional
        read_seq = read_seq.rstrip('\n') # Strip of newline character
        #seq = seq + read_seq
        out_file.write(read_seq)        # Write the formatted sequence to outputfile
        #print(read_seq)

in_file.close()         # closing input file
out_file.close()        # closing output file


#print("python script2",filename, hdr_ct)
