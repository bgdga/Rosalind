#Problem:
#The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
    #DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
    #In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

    #Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
    #Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

    #Sample Dataset
    # >Rosalind_6404
    # CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
    # TCCCACTAATAATTCTGAGG
    # >Rosalind_5959
    # CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
    # ATATCCATTTGTCAGCAGACACGC
    # >Rosalind_0808
    # CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
    # TGGGAACCTGCGGGCAGTAGGTGGAAT

    # Sample Output
    # Rosalind_0808
    # 60.919540

#Solution (4th trial): Finally, as per questions requirement (ChatGPT help, but I can Understand the code it gave and used as my requirement).

def read_fasta_file(filename):
    """
    Reads a text file in FASTA format and returns a list of DNA sequences.
    Each DNA sequence is represented as a tuple containing the sequence name (without the ">") and the sequence itself.
    """
    sequences = []
    with open(filename, 'r') as file:
        current_sequence = ('', '')
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                # Start of a new sequence
                if current_sequence[1]:
                    # Store the previous sequence
                    sequences.append(current_sequence)
                # Set the name of the new sequence
                name = line[1:]
                current_sequence = (name, '')
            else:
                # Add the current line to the current sequence
                current_sequence = (current_sequence[0], current_sequence[1] + line)
        # Store the last sequence
        sequences.append(current_sequence)
    return sequences

filename = input('Enter the PATH of the FASTA file: ')
sequences = read_fasta_file(filename)

# Calculate the GC content for each sequence
gc_content_list = []
for sequence in sequences:
    gc_count = sequence[1].count('G') + sequence[1].count('C')
    total_count = len(sequence[1])
    gc_content = gc_count / total_count * 100
    gc_content_list.append(gc_content)

# Print the GC content for each sequence
for i in range(len(sequences)):
    print(f"{sequences[i][0]}: GC content = {gc_content_list[i]:.6f}%")

# Find the sequence with the maximum GC content
max_gc_content = max(gc_content_list)
max_gc_content_index = gc_content_list.index(max_gc_content)
max_gc_content_sequence = sequences[max_gc_content_index]

# Print the sequence with the maximum GC content
print(f"{max_gc_content_sequence[0]} has the highest GC content of {max_gc_content:.6f}%")

#Print as the format asking in question
print(f"{max_gc_content_sequence[0]}")
print(f"{max_gc_content:.6f}%")




























#SOLUTION 3: not complete, only taking fasta format file as input.

import os

# Prompt the user for a file path
file_path = input("Enter the file path: ")

# Check if the file exists
if os.path.exists(file_path):
    # Open the file and read its contents into a list
    with open(file_path) as file:
        contents = file.readlines()

    # Print the contents of the file as a list
    print(contents)
else:
    print("File does not exist")

bases=('A','T','G','C')




#Solution 2: Still Not effecient, take sequance withought making any function.
from numpy import *
all_seq=[]
n=(int(input("please enter the number of sequances you want to enter")))
if n>10:
    print ("maximum number of allowed sequance is 10")
else:
    for i in range (n):
        a=array(input("please enter your copied FASTA file"))
        b=a.flatten()
        all_seq.append(''.join(b))
        i += 1





#SOLUTION 1. #defining function to ask user for input sequance. Needed because 10 strings are asked.
#note: it will take work on a single string nucleotides entry only, not extra data attahed to it.)
#it's very raw code, and uses many memory space. Needed to make it efecient.
def es():                                                                                                               #es=enter sequence, s= sequence
    s = (input("please enter your query nucleotide sequence only:"))
    if len(s) > 1000:
        print("Base number out of range. Maximum capacity 1000 bases. Please enter the query sequence under this limit")
        es()                                                                                                            #using recursion to ask user to enter again
    else:
        return list(s)
all_seq=[]
n=(int(input("please enter the number of sequances you want to enter")))
if n>10:
    print ("maximum number of allowed sequance is 10")
else:
    for i in range (n):
        a=es()
        all_seq.append(''.join(a))
        i += 1

#print(all_seq)
all=''.join(all_seq)
#print(all)
finalseq=list(all)
#print(finalseq)
gc_count=finalseq.count("G")+finalseq.count("C")
#print(gc_count)
gc_percent=(gc_count/len(all))*100
#print(gc_percent)
gc_round6=round(gc_percent,6)                                                                                                #round offs the gc count upto 6 decimal points.

#following is final answer print to given question
print(input("please enter your last fasta format name"))
print(gc_round6)




















