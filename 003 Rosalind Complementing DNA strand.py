#Problem :
#In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'. The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
#Given: A DNA string s of length at most 1000 bp. Return: The reverse complement sc of s.
#Solution- Here, complement is to be made, and then it is to be reversed in order... reverse complement.
#Most effecient (sapce required same, time to run is less)-

s=(input("please enter your query nucleotide sequence:"))
if len(s) > 1000:
    print("Base number out of range. Maximum capacity 1000 bases. Please enter the query sequence under this limit")
else:
    print(s.replace("A","B").replace("C","D").replace("T","A").replace("G","C").replace("B","T").replace("D","G")[::-1])




print('_'*100) #ignore;just to mark the end of above code on running it.
#less efficient (3 memory space used:- query seq s, modifid seq sc, reversed seq scr)



s=(input("please enter your query nucleotide sequence:"))                                                                 #s=seq
if len(s) > 1000:
    print("Base number out of range. Maximum capacity 1000 bases. Please enter the query sequence under this limit")
else:
    sc=s.replace("A","B").replace("C","D").replace("T","A").replace("G","C").replace("B","T").replace("D","G")            #sc=seq complement
    scr=sc[::-1]                                                                                                          #scr=seq compl reverse
    print(scr)


























print('_'*100) #ignore;just to mark the end of above code on running it.
#trying to use a self-defined function. Space used same- 3 memory. Time used my be less.



#defining function.
def c(s):                                                                                                                  #c=complement, s=sequance
    s=s.upper()                                                                                                            #accepts entry in upper case letters only. ATGCN not atgcn
    bc={'A':'T','C':'G','T':'A','G':'C','N':'N'}                                                                           #bc=base complement dictionary
    a=list(s)                                                                                                              #converting the given string into list named a
    a=[bc[b] for b in a]                                                                                                   #b= variable for components of set bc, replacing one base by other of given seq list form, and making complemented list.
    return ''.join(a)                                                                                                      #joins the components of list a (complemented of given seq) and makes a string, returns to called function

#calling/using defined function
s=(input("please enter your query nucleotide sequence:"))
if len(s) > 1000:
    print("Base number out of range. Maximum capacity 1000 bases. Please enter the query sequence under this limit")
else:
    sc=c(s)                                                                                                                     #sc=seq complement
    print(sc[::-1])                                                                                                             #printing reverse order of complement by adding [::-1] command









