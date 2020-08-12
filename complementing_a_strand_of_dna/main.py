"""
Complementing a Strand of DNA

Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

def reverse_complement_dna_strand(strand):
    trans_table = strand.maketrans("ATCG", "TAGC")
    reverse_strand = "".join(reversed(strand))
    return reverse_strand.translate(trans_table)

def main():
    with open('rosalind_revc.txt') as f:
        results = reverse_complement_dna_strand(f.read())
    print(results)

if __name__ == '__main__':
    main()

