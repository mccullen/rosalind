# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
# 
# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all 
# occurrences of 'T' in t with 'U' in u.
# 
# Given: A DNA string t having length at most 1000 nt.
# 
# Return: The transcribed RNA string of t.

import sys

def transcribe_into_dna(rna_sequence):
    rna_sequence = rna_sequence.upper()
    return rna_sequence.replace("T", "U")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python {0} <path-to-rna-sequence> <output-path>".format(sys.argv[0]))
        sys.exit(1)

    with open(sys.argv[1], "r") as rna_input, open(sys.argv[2], "w") as dna_output:
        rna_sequence = rna_input.read()
        dna_sequence = transcribe_into_dna(rna_sequence)
        dna_output.write(dna_sequence)