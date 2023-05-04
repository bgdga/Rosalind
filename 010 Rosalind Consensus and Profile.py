""" Problem: Finding a Most Likely Common Ancestor
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

Sample Dataset
                >Rosalind_1
                ATCCAGCT
                >Rosalind_2
                GGGCAACT
                >Rosalind_3
                ATGGATCT
                >Rosalind_4
                AAGCAACC
                >Rosalind_5
                TTGGAACT
                >Rosalind_6
                ATGCCATT
                >Rosalind_7
                ATGGCACT
Sample Output
                ATGCAACT
                A: 5 1 0 0 5 5 0 0
                C: 0 0 1 4 2 0 6 1
                G: 1 1 6 3 0 1 0 0
                T: 1 5 0 0 0 1 1 6
"""
#Solution trial 5. working. Output formatted as question. File saved as txt & pdf (PDF CODE NOT OPTIMISED). AI use.
import os
from fpdf import FPDF

# Ask user to input the path to the fasta file
filepath = input("Enter the path to the fasta file: ")

# Read fasta sequences from file
with open(filepath) as f:
    raw_file = f.read()
sequences = [seq.strip().upper()[:1000] for seq in raw_file.split(">")[1:] if len(seq.strip()) > 0]

# Check if number of sequences is greater than 10
if len(sequences) > 10:
    print("Error: More than 10 sequences found in the file. Please provide a file with up to 10 sequences.")
else:
    # Convert DNA sequences into a matrix
    matrix = []
    for seq in sequences:
        # Skip header line and concatenate the rest of the lines in the sequence
        seq_lines = seq.split("\n")[1:]
        seq = "".join(seq_lines)
        row = [base for base in seq]
        matrix.append(row)

    # Check if any sequence has more than 1000 bases
    if any(len(seq) > 1000 for seq in sequences):
        print("Error: One or more sequences in the file exceed the 1000 base limit.")
    else:
        # Count ATGC numbers per column and generate ATGC table
        atgc_table = {"A": [], "C": [], "G": [], "T": []}
        for j in range(len(matrix[0])):
            col = [row[j] for row in matrix]
            atgc_table["A"].append(str(col.count("A")))
            atgc_table["T"].append(str(col.count("T")))
            atgc_table["G"].append(str(col.count("G")))
            atgc_table["C"].append(str(col.count("C")))

        # Create consensus DNA sequence with bases with the highest value per column
        consensus_seq = ""
        for j in range(len(matrix[0])):
            col = [row[j] for row in matrix]
            max_base = max(atgc_table, key=lambda x: atgc_table[x][j])
            consensus_seq += max_base

        # Print ATGC_table and consensus DNA sequence
        atgc_string = "A: " + " ".join(atgc_table["A"]) + "\nC: " + " ".join(atgc_table["C"]) + "\nG: " + " ".join(atgc_table["G"]) + "\nT: " + " ".join(atgc_table["T"])
        print(consensus_seq)
        print(atgc_string)

        # Ask user to input the output directory path and filename
        output_dir = input("Enter the output directory path: ")
        output_filename = input("Enter the output filename (without extension): ")

        # Save output as txt file
        with open(os.path.join(output_dir, output_filename + ".txt"), "w") as f:
            f.write(consensus_seq + "\n" + atgc_string)

        # Save output as pdf file using FPDF library
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Consensus DNA Sequence:\n" + consensus_seq, ln=1)
        pdf.cell(200, 10, txt="ATGC Table:\n" + "A: " + " ".join(atgc_table["A"]), ln=3)
        pdf.cell(200, 10, txt="ATGC Table:\n" + "C: " + " ".join(atgc_table["C"]), ln=4)
        pdf.cell(200, 10, txt="ATGC Table:\n" + "G: " + " ".join(atgc_table["G"]), ln=5)
        pdf.cell(200, 10, txt="ATGC Table:\n" + "T: " + " ".join(atgc_table["T"]), ln=6)

        pdf.output(os.path.join(output_dir, output_filename + ".pdf"))
        print("Output saved successfully!")









































#Solution trial 4: Working. Saves the output file in directory (First time trying), AI help.
#OUTPUT IN LIST FORMAT, QUESTION DEMAND- String format

import os

# Ask user to input the path to the fasta file
filepath = input("Enter the path to the fasta file: ")

# Read fasta sequences from file
with open(filepath) as f:
    raw_file = f.read()
sequences = [seq.strip().upper()[:1000] for seq in raw_file.split(">")[1:] if len(seq.strip()) > 0]

# Check if number of sequences is greater than 10
if len(sequences) > 10:
    print("Error: More than 10 sequences found in the file. Please provide a file with up to 10 sequences.")
else:
    # Convert DNA sequences into a matrix
    matrix = []
    for seq in sequences:
        # Skip header line and concatenate the rest of the lines in the sequence
        seq_lines = seq.split("\n")[1:]
        seq = "".join(seq_lines)
        row = [base for base in seq]
        matrix.append(row)

    # Check if any sequence has more than 1000 bases
    if any(len(seq) > 1000 for seq in sequences):
        print("Error: One or more sequences in the file exceed the 1000 base limit.")
    else:
        # Count ATGC numbers per column and generate ATGC table (group of 4 lists).
        atgc_table = {"A": [], "C": [], "G": [], "T": []}
        for j in range(len(matrix[0])):
            col = [row[j] for row in matrix]
            atgc_table["A"].append(col.count("A"))
            atgc_table["T"].append(col.count("T"))
            atgc_table["G"].append(col.count("G"))
            atgc_table["C"].append(col.count("C"))

        # Create consensus DNA sequence (STRING FORMAT) with bases with the highest value per column
        consensus_seq = ""
        for j in range(len(matrix[0])):
            col = [row[j] for row in matrix]
            max_base = max(atgc_table, key=lambda x: atgc_table[x][j])
            consensus_seq += max_base

        # Print ATGC_table (LIST FORMAT) and consensus DNA sequence (STRING FORMAT)
        #print("Consensus DNA Sequence:")
        print(consensus_seq)
        #print("ATGC Table: as in question format")
        print("A:", atgc_table["A"])
        print("C:", atgc_table["C"])
        print("G:", atgc_table["G"])
        print("T:", atgc_table["T"])

        # Ask user to input the directory path to save the output file
        save_dir = input("Enter the directory path to save the output file: ")

        # Save output to a file in the user's specified directory
        filename = os.path.join(save_dir, "Rosalind_010_output.txt")
        with open(filename, "w") as f:
            #f.write("Consensus DNA Sequence: " + "\n")
            f.write(consensus_seq + "\n")
            #f.write("ATGC Table:\n")
            f.write("A: " + str(atgc_table["A"]) + "\n")
            f.write("C: " + str(atgc_table["C"]) + "\n")
            f.write("G: " + str(atgc_table["G"]) + "\n")
            f.write("T: " + str(atgc_table["T"]))

            print(f"Output saved to {filename}")






#Solution trial 3:Working. AI help. Header line of FASTA automatically removed (see trial 2).

# Ask user to input the path to the fasta file
filepath = input("Enter the path to the fasta file: ")

# Read fasta sequences from file
with open(filepath) as f:
    raw_file = f.read()
sequences = [seq.strip().upper()[:1000] for seq in raw_file.split(">")[1:] if len(seq.strip()) > 0]

# Check if number of sequences is greater than 10
if len(sequences) > 10:
    print("Error: More than 10 sequences found in the file. Please provide a file with up to 10 sequences.")
else:
    # Convert DNA sequences into a matrix
    matrix = []
    for seq in sequences:
        # Skip header line and concatenate the rest of the lines in the sequence
        seq_lines = seq.split("\n")[1:]                                                                                  #\n... to know ! this and next line are the commands which are removing the header from fasta file.
        seq = "".join(seq_lines)
        row = [base for base in seq]
        matrix.append(row)

    # Check if any sequence has more than 1000 bases
    if any(len(seq) > 1000 for seq in sequences):
        print("Error: One or more sequences in the file exceed the 1000 base limit.")
    else:
        # Count ATGC numbers per column and generate ATGC table
        atgc_table = {"A": [], "T": [], "G": [], "C": []}
        for j in range(len(matrix[0])):
            col = [row[j] for row in matrix]
            atgc_table["A"].append(col.count("A"))
            atgc_table["T"].append(col.count("T"))
            atgc_table["G"].append(col.count("G"))
            atgc_table["C"].append(col.count("C"))

        # Create consensus DNA sequence with bases with the highest value per column
        consensus_seq = ""
        for j in range(len(matrix[0])):
            col = [row[j] for row in matrix]
            max_base = max(atgc_table, key=lambda x: atgc_table[x][j])
            consensus_seq += max_base

        # Print ATGC table and consensus DNA sequence
        print("Consensus DNA Sequence:", consensus_seq)
        #print("ATGC Table: as in question format")
        print("A:", atgc_table["A"])
        print("C:", atgc_table["C"])
        print("G:", atgc_table["G"])
        print("T:", atgc_table["T"])











#Solution trial 2: AI help. Not giving required output.
#Troubleshoot: May be due to header of FASTA is getting counted in matrix formation from string output.

# Ask user to input the path to the fasta file
filepath = input("Enter the path to the fasta file: ")

# Read fasta sequences from file
with open(filepath) as f:
    raw_file = f.read()
sequences = [seq.strip().upper()[:1000] for seq in raw_file.split(">")[1:] if len(seq.strip()) > 0]

# Check if number of sequences is greater than 10
if len(sequences) > 10:
    print("Error: More than 10 sequences found in the file. Please provide a file with up to 10 sequences.")
else:
    # Convert DNA sequences into a matrix
    matrix = []
    for seq in sequences:
        row = [base for base in seq]
        matrix.append(row)

    # Check if any sequence has more than 1000 bases (not needed, because during splitting the input file into sequences, only first 1000 bases has been taken, already in initial steps).
    #if any(len(seq) > 1000 for seq in sequences):
        #print("Error: One or more sequences in the file exceed the 1000 base limit.")

    else:
        # Count ATGC numbers per column and generate ATGC table
        atgc_table = {"A": [], "T": [], "G": [], "C": []}
        for j in range(len(matrix[0])):
            col = [row[j] for row in matrix]
            atgc_table["A"].append(col.count("A"))
            atgc_table["T"].append(col.count("T"))
            atgc_table["G"].append(col.count("G"))
            atgc_table["C"].append(col.count("C"))

        # Create consensus DNA sequence with bases with the highest value per column
        consensus_seq = ""
        for j in range(len(matrix[0])):
            col = [row[j] for row in matrix]
            max_base = max(atgc_table, key=lambda x: atgc_table[x][j])                      #lambda key_to know yet, how it works !
            consensus_seq += max_base

        # Print ATGC table and consensus DNA sequence
        #print("ATGC Table:")
        print("Consensus DNA Sequence:", consensus_seq)
        print("A:", atgc_table["A"])
        print("T:", atgc_table["T"])
        print("G:", atgc_table["G"])
        print("C:", atgc_table["C"])












#Solution: Trial 1. AI help. not convenient to use. not tested/used.

# Ask user to input fasta format DNA sequences
num_seqs = 10 # You can change this to the number of sequences you want to input
sequences = []
for i in range(num_seqs):
    seq = input(f"Enter sequence {i+1} in fasta format: ")
    if seq.startswith(">"): # Ignore fasta headers
        continue
    seq = seq.upper().strip()[:1000] # Keep only first 1000 bases and convert to uppercase
    sequences.append(seq)

# Convert DNA sequences into a matrix
matrix = []
for seq in sequences:
    row = [base for base in seq]
    matrix.append(row)

# Count ATGC numbers per column and generate ATGC table
atgc_table = {"A": [], "T": [], "G": [], "C": []}
for j in range(len(matrix[0])):
    col = [row[j] for row in matrix]
    atgc_table["A"].append(col.count("A"))
    atgc_table["T"].append(col.count("T"))
    atgc_table["G"].append(col.count("G"))
    atgc_table["C"].append(col.count("C"))

# Create consensus DNA sequence with bases with the highest value per column
consensus_seq = ""
for j in range(len(matrix[0])):
    col = [row[j] for row in matrix]
    max_base = max(atgc_table, key=lambda x: atgc_table[x][j])
    consensus_seq += max_base

# Print ATGC table and consensus DNA sequence
print("ATGC Table:")
print("A:", atgc_table["A"])
print("T:", atgc_table["T"])
print("G:", atgc_table["G"])
print("C:", atgc_table["C"])
print("Consensus DNA Sequence:", consensus_seq)





















