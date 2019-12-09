#!/usr/bin/env python3

#step4 by Chandra Sarkar
### select files with sequences which have no stop codons

######### Importing required modules #########
import sys
import os
##############################################

######### Setting up arguments and filenames and Initializing the script #############
input_file_path = os.path.join(sys.argv[1])
in_file = open(input_file_path,'r')

filename = os.path.basename(input_file_path)
filename = filename.strip('.txt')

output_folder_path = os.path.join(sys.argv[2],filename+'.txt')
out_file = open(output_folder_path, 'w')

stop_codons = ['TAA','TGA','TAG']           # Declaring the list of stop codons
#######################################################################################

for line in in_file:            # For each line in the file

    if line.startswith('>'):         # If the line is a header line, then do:
        hdr = line                      # Set header line apart
        seq = str(in_file.readline())
        seq = seq.strip('\n')
        #print(seq)

        end_codon = seq[-3:]            # Get the last 3 letters of the sequence and assign to variable
        #print(end_codon)

        if end_codon in stop_codons:    # If end codon exist,
            #ctr_withstop += 1
            seq = seq[0:-3]             # Get rid of end codon 
            out_file.write('\n%s'%hdr)  # Write the header
            out_file.write(seq)         # Write the modified sequence

        elif end_codon not in stop_codons:      # If end codon not present
            #ctr_withoutstop += 1
            out_file.write('\n%s'%hdr)          # Write the header
            out_file.write(seq)                 # Write the sequence
                
in_file.close()         # closing input file
out_file.close()        # closing output file

