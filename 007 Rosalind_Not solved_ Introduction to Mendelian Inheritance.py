"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele
(and thus displaying the dominant phenotype). Assume that any two organisms can mate.
Sample Dataset       2 2 2
Sample Output        0.78333
"""
#Solution trial 5 (total time till this time used in solving this problem =almost 1 day) :
# Self made+(using AI, but quit logical answer) Still, outcome not matched to questions sample outcome.
# It may be the question itself has wrong data.

k, m, n = map(int, input("please enter the k_m_n, values; by entering space button in between: ").split())

t = k + m + n

p1 = k / t
p2 = m / t
p3 = n / t

p21 = k / (t - 1)
p22 = (m - 1/4) / (t - 1)
p23 = n / (t - 1)

p_dom = (p1 * p21) + (p1 * p22) + (p1 * p23) + (p2 * p21) + (3/4 * p2 * p22) \
        + (1/2 * p2 * p23) + (p3 * p21) + (1/2 * p3 * p22)

print(p_dom)



"""
k, m, n = map(int, input().split())
total = k + m + n

# Probability of choosing a homozygous dominant individual for the first parent
prob_homo_dominant = k / total

# Probability of choosing a heterozygous individual for the first parent
prob_heterozygous = m / total

# Probability of choosing a homozygous recessive individual for the first parent
prob_homo_recessive = n / total

# Probabilities of choosing the second parent based on the first parent's genotype
# If the first parent is homozygous dominant
prob_second_parent_homo_dominant = (k - 1) / (total - 1)
prob_second_parent_heterozygous = m / (total - 1)
prob_second_parent_homo_recessive = n / (total - 1)

# If the first parent is heterozygous
prob_second_parent_homo_dominant = k / (total - 1)
prob_second_parent_heterozygous = (m - 1/4) / (total - 1)
prob_second_parent_homo_recessive = n / (total - 1)

# If the first parent is homozygous recessive
prob_second_parent_homo_dominant = k / (total - 1)
prob_second_parent_heterozygous = m / (total - 1)
prob_second_parent_homo_recessive = (n - 1) / (total - 1)

# Probability of the offspring having a dominant allele
prob_dom_offspring = (prob_homo_dominant * prob_second_parent_homo_dominant) \
                     + (prob_homo_dominant * prob_second_parent_heterozygous) \
                     + (prob_homo_dominant * prob_second_parent_homo_recessive) \
                     + (prob_heterozygous * prob_second_parent_homo_dominant) \
                     + (3/4 * prob_heterozygous * prob_second_parent_heterozygous) \
                     + (1/2 * prob_heterozygous * prob_second_parent_homo_recessive) \
                     + (prob_homo_recessive * prob_second_parent_homo_dominant) \
                     + (1/2 * prob_homo_recessive * prob_second_parent_heterozygous)

print(prob_dom_offspring)

The reason we subtract 1/4 from m instead of just subtracting 1 is because heterozygous individuals have a 50% chance of passing on the dominant allele and a 50% chance of passing on the recessive allele. Therefore, when a heterozygous individual is chosen as the first parent, there is a 1/2 probability of passing on the dominant allele, and a 1/2 probability of passing on the recessive allele.
When the second parent is chosen, there are three possible scenarios: the second parent is homozygous dominant, heterozygous, or homozygous recessive. In the case where the second parent is heterozygous, there is a 1/4 probability that they will pass on the recessive allele to the offspring, and a 3/4 probability that they will pass on the dominant allele or the allele for heterozygosity.
So, to calculate the probability of choosing a heterozygous individual as the second parent, we need to subtract 1/4 from the total number of heterozygous individuals (m), since 1/4 of them will pass on the recessive allele. Hence, we get prob_second_parent_heterozygous = (m - 1/4) / (total - 1).

"""





#Solution Trial 4: Using raw formula (not simlified, bcz may be error by AI in simplifying it). Even this is not giving correct result. THe concept explained by AI to calculate it, turned out to be wrong.

# User input for population types
k=int(input("Enter the k-value: number of homozygous dominant: "))
m=int(input("Enter the m-value: number of heterozygous: "))
n=int(input("Enter the n-value: number of homozygous recessive: "))

p1=(k/(k+m+n)) * ((k-1)/(k+m+n-1))
p2=(k/(k+m+n)) * (m/(k+m+n-1))
p3=(k/(k+m+n)) * (n/(k+m+n-1))
p4=(m/(k+m+n)) * ((m-1)/(k+m+n-1))
p5=(m/(k+m+n)) * (n/(k+m+n-1))
#p6=(n/(k+m+n)) * ((n-1)/(k+m+n-1))

P_dominant=p1+p2+p3+p4+p5
#print(p1,p2,p3,p4,p5)
print(f"{P_dominant:.5f}")



#SOLUTION: Trial 3. AI help.

def dominant_probability(k, m, n):
    total = k + m + n
    numerator = (k*(k-1)) + (2*k*m) + (2*k*n) + (0.75*m*(m-1)) + (0.5*m*n)
    denominator = total * (total - 1)
    return numerator / denominator

# User input for population types
k=int(input("Enter the k-value: number of homozygous dominant: "))
m=int(input("Enter the m-value: number of heterozygous: "))
n=int(input("Enter the n-value: number of homozygous recessive: "))

# Call the function to get the probability of producing an offspring with a dominant allele
prob = dominant_probability(k, m, n)

print("Probability of producing an offspring with a dominant allele: ", f"{prob:.5f}")




#SOLUTION: Trial 2. AI help for formula. Working but not expected result. somewhere mistake by AI in creating in Formula.

# User input for population types
k=int(input("Enter the k-value: number of homozygous dominant: "))
m=int(input("Enter the m-value: number of heterozygous: "))
n=int(input("Enter the n-value: number of homozygous recessive: "))

# Probability of dominant phenotype offspring (P)
P=((k*(k-1)) + (2*k*m) + (2*k*n) + (0.75*m*(m-1)) + (0.5*m*n))/((k+m+n)*(k+m+n-1))
print(f"{P:.5f}")


"""
To calculate above formula, following logic has been used (Chat GPT AI ): looks reasonable, let's try...
To calculate the probability that two randomly selected organisms will produce an individual with a dominant allele, we can use the principles of Mendelian genetics.
Let's first consider the possible genotypes of the individuals in the population:
Homozygous dominant: AA
Heterozygous: Aa
Homozygous recessive: aa
When two organisms mate, they each contribute one of their alleles to their offspring. Therefore, we can use a Punnett square to determine the possible genotypes of their offspring and their corresponding probabilities.
For simplicity, let's assume that the population is large enough that we can use the laws of probability to calculate the likelihood of any two organisms mating.
Let's consider the different possible pairings of organisms and their probabilities:

1. AA x AA: All offspring will be homozygous dominant (AA) and will display the dominant phenotype. The probability of this pairing is (k/k+m+n) * ((k-1)/(k+m+n-1)), since the probability of selecting an AA individual for the first parent is k out of the total population, and the probability of selecting another AA individual for the second parent is (k-1) out of the remaining individuals.
2. AA x Aa: All offspring will be heterozygous (Aa) and will display the dominant phenotype. The probability of this pairing is (k/k+m+n) * (m/(k+m+n-1)) or ((m/k+m+n) * (k/(k+m+n-1)), since there are two possible orders in which the parents can be selected.
3. AA x aa: All offspring will be heterozygous (Aa) and will display the dominant phenotype. The probability of this pairing is (k/k+m+n) * (n/(k+m+n-1)) or ((n/k+m+n) * (k/(k+m+n-1))), since there are two possible orders in which the parents can be selected.
4. Aa x Aa: 75% of the offspring will be heterozygous (Aa) and display the dominant phenotype, while 25% will be homozygous recessive (aa) and display the recessive phenotype. The probability of this pairing is (m/k+m+n) * ((m-1)/(k+m+n-1)), since there are m possible Aa individuals for the first parent and m-1 possible Aa individuals for the second parent.
5. Aa x aa: 50% of the offspring will be heterozygous (Aa) and display the dominant phenotype, while 50% will be homozygous recessive (aa) and display the recessive phenotype. The probability of this pairing is (m/k+m+n) * (n/(k+m+n-1)) or ((n/k+m+n) * (m/(k+m+n-1))), since there are two possible orders in which the parents can be selected.
6. aa x aa: All offspring will be homozygous recessive (aa) and display the recessive phenotype. The probability of this pairing is (n/k+m+n) * ((n-1)/(k+m+n-1)), since the probability of selecting an aa individual for the first parent is n out of the total population, and the probability of selecting another aa individual for the second parent is (n-1) out of the remaining individuals.
To calculate the overall probability of producing an offspring with a dominant allele, we can sum the probabilities of all the pairings that produce at least one offspring with the dominant phenotype (pairings 1, 2, 3, 4 and 5):

P(dominant) = [(k/k+m+n) * ((k-1)/(k+m+n-1))]    +    [(k/k+m+n) * (m/(k+m+n-1))]    +    [(k/k+m+n) * (n/(k+m+n-1))]     +   [(m/k+m+n) * ((m-1)/(k+m+n-1))]     +     [(m/k+m+n) * (n/(k+m+n-1))]
simplified: P(dominant) = [k(k-1) + 2km + 2kn + 0.75m(m-1) + 0.5mn] / [(k+m+n)(k+m+n-1)]

"""


#SOLUTION: Trial 1. AI help for probability formula: Using Hardy weinberg equation. WORKING BUT RESULT NOT AS GIVEN IN QUESTION'S SAMPLE DATA.

# User input for population types
k=int(input("Enter the k-value: number of homozygous dominant: "))
m=int(input("Enter the m-value: number of heterozygous: "))
n=int(input("Enter the n-value: number of homozygous recessive: "))

# Total population size (N)
N=k+m+n

# Frequencies of dominant (p) and recessive (q) alleles
p=(2*k+m)/(2*N)
q=(2*n+m)/(2*N)

# Probability of dominant phenotype offspring (P): AS PER P2+2PQ+Q2
P=p**2+2*p*q

print(P)


