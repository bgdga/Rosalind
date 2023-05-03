"""
Problem
Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s (as a result, t must be no longer than s).
The position of a symbol in a string is the total number of symbols found to its left, including itself
(e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18).
The symbol at position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s; for example,
if s= "AUGCUUCAGAAAGGUCUUACG", then s[2:5]= "UGCU".
The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it occurs more than once as a substring of s (see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.

Sample Dataset                GATATATGCATATACTT
                              ATAT
Sample Output                 2 4 10
"""


#solution trial4: AI help in loop: worked.

def find_dna_motif(dna_seq, motif):
    """
    Finds a given DNA motif in a given DNA sequence.

    Args:
    - dna_seq (str): a DNA sequence
    - motif (str): a DNA motif to search for

    Returns:
    - A list of starting indices of the motif in the sequence (0-based).
    """

    indices = " "
    i = 0
    while i < len(dna_seq):
        index = dna_seq.find(motif, i)
        if index == -1:  # motif not found
            break
        indices += str(index+1) + " "
        i = index + 1  # start searching after the last match
    return indices
#calling funcion

s=input("Hey, Enter the DNA sequence (s): ")
t=input("Now, Enter the query Motif sequence (t): ")
motif_indices=find_dna_motif(s,t)
print(motif_indices)












#Solution trial 3: While loop, using rna to protein code strategy. Not working.

s=input("plz Enter the DNA sequence: ")
motif=input("Please Enter the query Motif sequence: ")
t= {motif:motif}

m_pos=''
x=[]
i=0
while i<=len(s):
    m= s[i:i+len(motif)-1]
    pos= t[m]
    m_pos += pos
    x.append(i)
    i+=1
print(m_pos)




#Solution Trial 2: TRying using while loop, instead of for loop. Not working.

s=input("Please Enter the DNA sequence: ")
t=input("Please Enter the query Motif sequence: ")
#print(len(s), len(t))

o=[]
if len(s)>1000 or len(t)>1000 or len(t)>len(s):
    print ("Lenght of DNA/motif is out of range. Please enter max 1kbp length.")
else:
    i=0
    while i<=len(s)-(len(t)-1):
        motif= s[i:i+len(t)-1]
        t=motif
        o.append(i)
        i+=1
print(o)



#Solution: Trial 1- No AI use. Error showing- IndexError: string index out of range. Tried different ways,error resolved.. but output not showing.

s=input("Enter the DNA sequence: ")
t=input("Enter the query Motif sequence: ")
#print(len(s), len(t))

o=[]
if len(s)>1000 or len(t)>1000 or len(t)>len(s):
    print ("Lenght of DNA/motif is out of range. Please enter max 1kbp length.")
else:
   for i in range(len(s)-(len(t)-1)):
       if s[i:i+len(t)-1]==t:
           o.append(i)
           #print(i)
           i+=1
       else:
           continue
print(o)



