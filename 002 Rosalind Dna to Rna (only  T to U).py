#Problem
#An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'. Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u
#Given: A DNA string t  having length at most 1000 nt.     Return: The transcribed RNA string of t
#Solution- (most effecient)

dnaseq=(input("please enter your query nucleotide sequence:"))
if len(dnaseq) > 1000:
    print("Base number out of range. Maximum capacity 1000 bases. Please enter the query sequence under this limit")
else:
    rnaseq = dnaseq.replace("T", "U")
    print(rnaseq)




print('_'*100) #ignore;just to mark the end of above code on running it. Following is the less effecient code that I had created.


dnaseq=(input("please enter your query nucleotide sequence:"))
rnaseq=" "

if len(dnaseq) > 1000:
    print("Base number out of range. Maximum capacity 1000 bases. Please enter the query sequence under this limit")

else:
    for base in dnaseq:
        if base in "ACGU":
            rnaseq+=base
        else:
            rnaseq+="U"
    print(rnaseq)




print('_'*100) #ignore;just to mark the end of above code on running it. Following is the raw code that I had created.


dnaseq=(input("please enter your query nucleotide sequence:"))
bases=[a for a in "ACGU"]
rnaseq=[]

if len(dnaseq) > 1000:
    print("Base number out of range. Maximum capacity 1000 bases. Please enter the query sequence under this limit")

else:
    for i in range(len(dnaseq)):
        base = dnaseq[i]
        if base in bases:
            rnaseq.append(base)
        else:
            rnaseq.append("U")
    print(rnaseq)
    rnaseq_cont =''.join(rnaseq)
    print(rnaseq_cont)

