# Problem
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of
# a string is the number of symbols that it contains.
# 
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is 
# "ATGCTTCAGAAAGGTCTTACG."
# 
# Given: A DNA string s of length at most 1000 nt.
# 
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', 
# and 'T' occur in s.
# 
# Sample Dataset
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# Sample Output
# 20 12 17 21

def count_dna_nucleitoids(sequence):
    nAdenine = 0
    nCystosine = 0
    nGuanine = 0
    nThymine = 0
    for nucleobase in sequence:
        nucleobase = nucleobase.upper()
        if nucleobase == "A":
            nAdenine += 1
        elif nucleobase == "C":
            nCystosine += 1
        elif nucleobase == "G":
            nGuanine += 1
        elif nucleobase == "T":
            nThymine += 1
    return "{} {} {} {}".format(str(nAdenine), str(nCystosine), str(nGuanine), str(nThymine))
