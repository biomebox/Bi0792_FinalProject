#!/usr/bin/env python3

#step6 by Chandra Sarkar

######### Importing required modules #########
import sys
import os
##############################################

######### Setting up arguments and filenames and Initializing the script #############
input_file_path = os.path.join(sys.argv[1])
in_file = open(input_file_path,'r')

filename = os.path.basename(input_file_path)
filename = filename.strip('.txt')

output_folder_path_1 = os.path.join(sys.argv[2],'organism1_sequences.txt')  # Refer to this output file
output_folder_path_2 = os.path.join(sys.argv[2],'organism2_sequences.txt')  # Refer to this output file
#######################################################################################

for line in in_file:                    # For each line in the file
    
    if line.startswith('>'):            # If the line is a header line, then do
        hdr_1 = line                    # Set header line apart
        hdr_1 = hdr_1.strip('\n')
        DNA_sqn1 = in_file.readline()
        DNA_sqn1 = DNA_sqn1.strip('\n')
        
        hdr_2 = in_file.readline()
        hdr_2 = hdr_2.strip('\n')
        DNA_sqn2 = in_file.readline()
        DNA_sqn2 = DNA_sqn2.strip('\n')

out_file_1 = open(output_folder_path_1, 'a')   # Open the file to append instead of write
out_file_1.write("%s\n"%hdr_1)                 # Write the header for the organism in focus
out_file_1.write("%s\n"%DNA_sqn1)              # Write their cooresponding prot sequence
out_file_1.close()      # closing output file

out_file_2 = open(output_folder_path_2, 'a')    # Open the file to append instead of write
out_file_2.write("%s\n"%hdr_2)                  # Write the header for the homologous organism in focus
out_file_2.write("%s\n"%DNA_sqn2)               # Write their cooresponding prot sequence
out_file_2.close()      # closing output file