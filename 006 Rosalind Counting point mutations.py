"""
Problem
Given two strings s and t of equal length, the Hamming distance (no. of bases different in 1 from other sequence) between s
and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t)

Sample Dataset     GAGCCTACTAACGGGAT
                   CATCGTAATGACGGCCT

Sample Output      7
"""
#Solution trial 3: Self made. Working. 1kbp limit applied. Time taken to code= 2 hrs. max time used in optimizing loop for finding unmatched bases and counting it+ finding out that if the loop is working with string input or list, entered value by typing one by one or copy paste etc (silly distracting things).
s=input("please enter the 1st (t) sequence: ")
t=input("please enter the 2nd (s) sequence: ")
if len(s)==len(t)<1001:
    s=list(s)
    t=list(t)
    print(s,t)
    h=0

    for i in range(len(s)):
        if s[i]==t[i]:
            continue
        else:
           globals()['h']+=1
    print(h)
else:
    print("Given sequences are out of range, or unequal length. PLease give sequences of equal length, max length per sequences is 1000 bases")

print(s)



















print("*"*200)

#Solution trial 2: Self made. Not giving correct output (dH).
x=input("please enter the 1st (t) sequence: ")
y=input("please enter the 2nd (s) sequence: ")
s=list(x)
t=list(y)
print(s,t)
h=0
i=1
while i<=len(s):
    if s==t:
        continue
    else:
        globals()['h']+=1
        s[i]=t[i]
    i+=1

print(h)


#Solution (Trial 1): Self-tried. NOt working.Not giving correct output (dH)

x=input("please enter the 1st (t) sequence: ")
y=input("please enter the 2nd (s) sequence: ")
s=list(x)
t=list(y)
print(s,t)
h=0
for a in s:
    if a in t:
        continue
    else:
       globals()['h']+=1
print(h)

