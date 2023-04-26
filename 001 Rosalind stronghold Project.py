#Problem
    #A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
    #An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
    #Given: A DNA string s of length at most 1000 nt.
    #Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
    #Sample Dataset-    AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
    #Sample Output    20 12 17 21
#solution
# #AFTER A LOT OF TRIALS AND ERRORS... 6 HOURS OF WORK, FINALLY CAME UP WITH A WORKING CODE.





seq=(input("please enter your query nucleotide sequence:"))
bases=[a for a in "ACGT"]
base_count = {base: 0 for base in bases}

if len(seq)>1000:
    print("Base number out of range. Maximum capacity 1000 bases. Please enter the query sequence under this limit")

else:
    for i in range(len(seq)):
        base=seq[i]
        if base in bases:
            base_count[base] += 1

    # Print the counts of ATGC
    for base, count in base_count.items():
        print(base, count)








print('_'*100) #ignore;just to mark the end of above code on running it.
#following are the codes that I tried to create but not worked... please ignore them!


seq=(input("please enter your query nucleotide sequence:"))
bases=[a for a in (seq)]
search=["A","T","G","C"]
base_count={"A":0, "T":0, "G":0, "C":0}
if len(bases)>1000:
    print("length of entered sequance is more than 1000. Please enter maximum 1000 bases")
    seq = (input("please enter your query nucleotide sequence:"))
else:
    for i in range(len(bases)):
        if bases in search:
            base_count[bases]+=1
print(bases)
print(base_count.keys, ":", base_count.values)

#*************************************************************************************************************************



seq=[]                                                                         #creating a blank list to get input from user
n=len(seq)<=1000                                                               #in the question, max 1000 base input limit is given
print("please enter your query sequance")
for i in range(1000):
    x = (input(":"))
    seq.append(x)
print("Your input sequance is:", seq)

#*************************************************************************************************************************************


from array import *

seq=array('i',[])                                                                        #creating a blank array to get input from user
n=int(input("Please enter lenght of your query sequance."
            "Note: max lenght should be 1000 bases :"))                                #in the question, max 1000 base input limit is given
if n>1000:
    print("Input out of range."
          "please enter lenght smaller than 1000")
    n = int(input(":"))
    for i in range(1):
        print("please enter your query sequance")
    for i in range(n):
        x=(input(":"))
        seq.append(x)
else:
    print("please enter your query sequance")
    for i in range(n):
        x = (input(":"))
        seq.append(x)
print("Your input sequance is:", seq)
