#!/usr/bin/env python3

#step5 by Chandra Sarkar
### Translating the DNA sequences into proteins using the Bio module in Python

######### Importing required modules #########
import sys
import os
from Bio.Seq import Seq #import Bio
##############################################

######### Setting up arguments and filenames and Initializing the script #############
input_file_path = os.path.join(sys.argv[1])
in_file = open(input_file_path,'r')

filename = os.path.basename(input_file_path)
filename = filename.strip('.txt')

output_folder_path = os.path.join(sys.argv[2],filename+'.txt')
out_file = open(output_folder_path, 'w')
#######################################################################################   

################# Main loop #################
for line in in_file:                        # For each line in the file

    if line.startswith('>'):                # If the line is a header line, then do
        hdr = line                          # Set header line apart
        DNA_sqn1 = str (in_file.readline()) # Read the next line i.e the sequence line follows the header
        DNA_sqn1 = DNA_sqn1.strip('\n')
        DNA_sqn = Seq(DNA_sqn1)
        pro_sqn = str (DNA_sqn.translate()) # Use the Bio Python to translate the DNA to protein
        out_file.write(hdr)
        out_file.write("%s\n"%pro_sqn)      # Write the protein sequence
##############################################

in_file.close()         # closing input file
out_file.close()        # closing output file
