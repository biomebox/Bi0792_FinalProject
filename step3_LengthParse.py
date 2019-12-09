#!/usr/bin/env python3

#step3 by Chandra Sarkar
### select files with sequences which are multiples of 3       

######### Importing required modules #########
import sys
import os
##############################################

######### Setting up arguments and filenames and Initializing the script #############
input_file_path = os.path.join(sys.argv[1]) # Read in the first argument from the bash wrapper
in_file = open(input_file_path,'r')         # Open the file for reading

filename = os.path.basename(input_file_path)     # Get the filename
filename = filename.strip('.txt')               # Modify filename

output_folder_path = os.path.join(sys.argv[2],filename+'.txt') # Read in the second argument from the bash wrapper and name the output file

#######################################################################################

#####   Reading each individual line and assigning it to a variable   ######
in_file.seek(1)
in_file_hdr1 = in_file.readline()
in_file_seq1 = in_file.readline()
in_file_seq1 = in_file_seq1.strip('\n')
in_file_seq1_len = len(in_file_seq1)
in_file_rem1 = in_file_seq1_len % 3      # The remainder when sequence lenght is divided by 3
    
in_file_hdr2 = in_file.readline()
in_file_seq2 = in_file.readline()
in_file_seq2 = in_file_seq2.strip('\n')
in_file_seq2_len = len(in_file_seq2)
in_file_rem2 = in_file_seq2_len % 3     # The remainder when sequence lenght is divided by 3
#############################################################################
'''
### For checkpoint ###
full= in_file.readlines()
full_len= len(full)
print(full_len)
######################
'''

################# Main loop #################  
if in_file_rem1 == 0 and in_file_rem2 == 0:     # If both the sequences are multiples of 3 i.e. remainder = 0,
    out_file = open(output_folder_path, 'w')    # Open the file for writing
    
    out_file.write(in_file_hdr1)                # Write the header to output file                
    out_file.write(in_file_seq1)                # Write the sequence to outputfile
        
    out_file.write("\n%s"%in_file_hdr2)         # Write the header to output file
    out_file.write(in_file_seq2)                # Write the formatted sequence to outputfile

    out_file.close()    # closing output file
############################################## 
       
in_file.close()     # closing input file



