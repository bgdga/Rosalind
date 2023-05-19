"""Problem
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2
and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months.
See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20     (not given - rate of reproduction, and rabbit pairs at start of counting. .I am considering both =1 to solve qn)
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
Sample Dataset    6 3
Sample Output      4
"""

# Solution trial (13): Future task. no more logic left with me to solve this question.















#Solution (12): New strategy. AI Help. not working yet correctly. 11/5/23
def calculate_rabbit_pairs(n, m):
    pairs = [0] * (n + 1)
    pairs[0] = 1
    pairs[1] = 1

    for i in range(2, n + 1):
        if i <= m:
            pairs[i] = pairs[i - 1] + pairs[i - 2]  # Fibonacci sequence
        else:
            pairs[i] = pairs[i - 1] + pairs[i - 2] - pairs[i - (m + 1)]  # Subtract pairs at the end of lifespan

    return pairs[n]

# Test the function
n, m = map(int, input("Enter the number of months and the lifetime: ").split())
result = calculate_rabbit_pairs(n, m)
print(f"The number of rabbit pairs remaining after {n} months is {result}.")







# Solution trial (11): Modification in 10th trial. Not working. #each trial= multiple modification (to & fro), and testing sample on each change. Each trial= minimum 30 mins used.

def fib(n, m):
    if n > 100 or n == 0 or m > 20:
        print("n-value or m-value out of range, required value n>0<=100 & m<=20, please enter a valid number")
    elif n == 1 or n == 2:
        print(1)
    else:
        for i in range(1, n + 1):
            c=[1,1]
            if i < m - 1 and i > 2:
                c[i] = (c[i - 2] + c[i - 1])
                c.append(c[i])
            if i > m - 1 and i > 2:
                for i in range(1, m):
                    c[i] = (c[i - 2] + c[i - 1])
                    c.append(c[i])

                    for i in range(m + 1, n + 1):
                        c[i] = (c[i - 2] + c[i - 1]) - c[i - (m - 1)]
                        c.append(c[i])
            print(c[-1])  # Print the last value of c

fib(int(input("enter N--- value: ")), int(input("enter M--- value: ")))







# Solution trial (10): Modification in 9th trial. Not working.

def fib(n, m):
    if n > 100 or n == 0 or m > 20:
        print("n-value or m-value out of range, required value n>0<=100 & m<=20, please enter a valid number")
    elif n == 1 or n == 2:
        print(1)
    else:
        a = [0] * n
        b = 1
        c = [0] * n  # Create a list to store the values of c
        for i in range(2, n):
            if m > i > 2:
                c[i] = (a[i - 2] + b)
                c.append(c[i])
                a[i] = b
                a.append(a[i])
                b = c[i]

            if i > m - 1 and i > 2:
                for i in range(2, m):
                    c[i] = (a[i - 2] + b)
                    c.append(c[i])
                    a[i] = b
                    a.append(a[i])
                    b = c[i]
                for i in range(m, n+1):
                    c[i] = (a[i - 2] + b) - a[i - m]
                    c.append(c[i])
                    a[i] = b
                    a.append(a[i])
                    b = c[i]

        print(c[-1])  # Print the last value of c


fib(int(input("enter N-- value: ")), int(input("enter M-- value: ")))





# Solution trial (9): Modification in 8th trial. Not working.

def fib(n, m):
    if n > 100 or n == 0 or m > 20:
        print("n-value or m-value out of range, required value n>0<=100 & m<=20, please enter a valid number")
    elif n == 1 or n == 2:
        print(00)
    else:
        a = [0] * n
        b = [1] * n
        c = [0] * n  # Create a list to store the values of c
        for i in range(1, n + 1):
            if m - 1 > i > 2:
                c[i] = (a[i - 2] + b[i - 1])
                c.append(c[i])
                a[i] = b[i]
                a.append(a[i])
                b[i] = c[i]
                b.append(b[i])
            if i > m - 1 and i > 2:
                for i in range(1, m):
                    c[i] = (a[i - 2] + b[i - 1])
                    c.append(c[i])
                    a[i] = b[i]
                    a.append(a[i])
                    b[i] = c[i]
                    b.append(b[i])
                for i in range(m + 1, n + 1):
                    c[i] = (a[i - 2] + b[i - 1]) - a[i - (m - 1)]
                    c.append(c[i])
                    a[i] = b[i]
                    a.append(a[i])
                    b[i] = c[i]
                    b.append(b[i])
        print(c[-1])  # Print the last value of c


fib(int(input("enter N- value: ")), int(input("enter M- value: ")))











# Solution trial (8): Modification in 7th trial. Not working.

def fib(n, m):
    if n > 100 or n == 0 or m > 20:
        print("n-value or m-value out of range, required value n>0<=100 & m<=20, please enter a valid number")
    elif n == 1 or n == 2:
        print(00)
    else:
        c = [0] * n  # Create a list to store the values of c
        for i in range(1, n + 1):
            if i < m - 1 and i > 2:
                c[i] = (c[i - 2] + c[i - 1])
                c.append(c[i])
            if i > m - 1 and i > 2:
                for i in range(1, m):
                    c[i] = (c[i - 2] + c[i - 1])
                    c.append(c[i])

                    for i in range(m + 1, n + 1):
                        c[i] = (c[i - 2] + c[i - 1]) - c[i - (m - 1)]
                        c.append(c[i])
        print(c[-1])  # Print the last value of c


fib(int(input("enter 'N' value: ")), int(input("enter 'M' value: ")))


# Solution trial (7): Modification in 6th trial. Not working.

def fib(n, m):
    a = 0
    b = 1
    c = [0] * n  # Create a list to store the values of c

    if n > 100 or n == 0 or m > 20:
        print("n-value or m-value out of range, required value n>0<=100 & m<=20, please enter a valid number")
    else:  # globals()['o']=c
        for i in range(1, n + 1):
            if i < m - 1:
                globals()['c'][i] = (globals()['a'] + globals()['b'])
                globals()['a'] = globals()['b']
                globals()['b'] = globals()['c'][i]
                globals()['c'].append(c[i])
            else:
                for i in range(1, m):
                    globals()['c'][i] = (globals()['a'] + globals()['b'])
                    globals()['a'] = globals()['b']
                    globals()['b'] = globals()['c'][i]
                    globals()['c'].append(globals()['c'][i])

                for i in range(m, n + 1):
                    globals()['c'][i] = (globals()['a'] + globals()['b']) - globals()['c'][i - (m - 1)]
                    globals()['a'] = globals()['b']
                    globals()['b'] = globals()['c'][i]
                    globals()['c'].append(globals()['c'][i])
    print(c[-1])  # Print the last value of c


fib(int(input("enter N value: ")), int(input("enter M value: ")))


# Solution trial (6): Modification in 5th trial. Not working.

def fib(n, m):
    if n > 100 or n == 0 or m > 20:
        print("n-value or m-value out of range, required value n>0<=100 & m<=20, please enter a valid number")
    else:
        a = 0
        b = 1
        c = [0] * n  # Create a list to store the values of c
        for i in range(1, n + 1):
            if i < m - 1:
                c[i] = (a + b)
                a = b
                b = c[i]
                c.append(c[i])
            else:
                for i in range(1, m):
                    c[i] = (a + b)
                    a = b
                    b = c[i]
                    c.append(c[i])
                # write a code to use a b cvalue from this for loop , continued to next for loop...

                for i in range(m, n + 1):
                    c[i] = (a + b) - c[i - (m - 1)]
                    a = b
                    b = c[i]
                    c.append(c[i])
        print(c[-1])  # Print the last value of c


fib(int(input("enter n value: ")), int(input("enter m value: ")))


# Solution trial (5): Modification in 4th trial. Not working.

def fib(n, m):
    if n > 100 or n == 0 or m > 20:
        print("n-value or m-value out of range, required value n>0<=100 & m<=20, please enter a valid number")
    else:
        if n < m:
            if n == 1 or n == 2:
                print(1)
            else:
                a = 1
                b = 1
                c = 0
                for i in range(2, n - 1):
                    print(i)
                    c = (a + b)
                    a = b
                    b = c
                print(c)
        else:
            a = 0
            b = 1
            c = [0] * n  # Create a list to store the values of c
            for i in range(n):
                c[i] = (a + b) - c[i - m]
                c.append(c[i])
                a = b
                b = c[i]
            print(c[-1])  # Print the last value of c


fib(int(input("enter n value: ")), int(input("enter m value: ")))


# Solution trial (4):
# my code+ AI : not working.


def fib(n, m):
    if n > 100 or n == 0 or m > 20:
        print("n-value or m-value out of range, required value n>0<=100 & m<=20, please enter a valid number")
    else:
        if n < m:
            a = 0
            b = 1
            c = 0
            for i in range(n):
                c = (a + b)
                a = b
                b = c
            print(c)
        else:
            a = 0
            b = 1
            c = [0] * n  # Create a list to store the values of c
            for i in range(n - 1):
                if i < m:
                    c[i] = (a + b)
                else:
                    c[i] = (a + b) - c[i - m]
                a = b
                b = c[i]
            print(c[-1])  # Print the last value of c


fib(int(input("enter n value: ")), int(input("enter m value: ")))


# SOLUTION trial (3): SElf & AI help. Spent 6+ hours, unale to get a correct code. uff !
# USING PURE FIBBONACCI FORMULA, modified to make it usefull for mortal rabits. (NOT MODIFIED AS ROSALIND 005).

def fib(n, m):
    sequence = [1, 1]  # Initialize the Fibonacci sequence with the first two values
    for i in range(2, n):
        c = (sequence[i - 1] + sequence[i - 2]) - sequence[i - m] if i >= m else sequence[i - 1] + sequence[i - 2]
        sequence.append(c)
    print(sequence[-1])  # Print the last number in the sequence


fib(int(input("Enter n value: ")), int(input("Enter m value: ")))


# my code:
def fib(n, m):
    a = 0
    b = 1
    c = 0
    for i in range(2, n):
        c = (a + b) - a[i - m]  # error here
        a = b
        b = c
    print(c)


fib(int(input("enter n value: ")), int(input("enter m value: ")))


# Solution (2): AI answer. Not working correctly.

def rabbit_pairs(n, m):
    # Initialize the list to store the number of rabbit pairs for each month
    pairs = [0] * n

    # Base cases
    pairs[0] = 1  # Number of pairs in the first month
    pairs[1] = 1  # Number of pairs in the second month

    for i in range(2, n):
        # Each new pair is born from the previous generation
        # The number of new pairs is equal to the number of pairs from two months ago
        new_pairs = pairs[i - 2]

        # Subtract the number of pairs that have lived for m months
        if i >= m:
            old_pairs = pairs[i - m]
            new_pairs -= old_pairs

        # Add the new pairs to the current month's total
        pairs[i] = pairs[i - 1] + new_pairs

    return pairs[-1]  # Return the number of pairs in the last month


# Example usage:
n, m = map(int, input("Enter the values of n and m: ").split())
result = rabbit_pairs(n, m)
print("Total number of pairs remaining after the n-th month:", result)

# Solution (1): modifying the code of Rosalind 005 problem (immortal fibbonaci rabbit). Not worked. Somewhere mistake. Will try on MONDAY...FRESH MIND.
# self_tip: write fibbnc - 4th prev gen variable.

n = int(input("Enter the n-value (months) as given in question: "))  # n=No_of_months
k = 1  # k=int(input("Enter k-value (reproduction per month) as given in Question: "))                      #k=Rabbit_rate_of_reproduction
o = 1  # o= output at given n,k
m = int(input("Enter the m-value (rabbit life, months) as given in question: "))

if n > 100 or n == 0 or m > 20:  # or k>5:
    print("n-value or m-value out of range, required value n>0<=100 & m<=20, please enter a valid number")
elif n < 3:
    print(o)
else:
    a = 1  # a=otal population at 1st month=1
    b = 1  # b= total population at 2nd month=1
    for i in range(n - 1):
        c = ((a * k) + b)  # c= total population at 3rd month (immortal)
        d = c - a  # d= total population at 3rd month (mortal)
        globals()['o'] = d
        a = b
        b = c
        c = d
    print(o)
