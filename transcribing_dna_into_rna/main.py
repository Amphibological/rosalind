"""
Transcribing DNA into RNA

Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""

def transcibe_dna_into_rna(string):
    return string.replace('T', 'U')

def main():
    with open('rosalind_rna.txt') as f:
        rna = transcibe_dna_into_rna(f.read())
    print(rna)

if __name__ == '__main__':
    main()
