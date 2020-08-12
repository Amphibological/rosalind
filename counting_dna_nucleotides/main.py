"""
Counting DNA Nulceotides

Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

"""

from collections import Counter

def count_dna_nucleotides(string):
    counter = Counter(string)
    return (
        counter['A'],
        counter['C'],
        counter['G'],
        counter['T']
    )

def main():
    with open('rosalind_dna.txt') as f:
        a, c, g, t = count_dna_nucleotides(f.read())
    print(f"{a} {c} {g} {t}")

if __name__ == '__main__':
    main()
