'''
Author: Ilja Lom...
GitHub: https://github.com/Ilja-Lom
Publication-Date: 24/09/2021
Description: 
    An algorithm to check for the number of transition, and transversion mutations between two homologous
    DNA sequences
'''
'''Initialising variables'''
transition = 0
transversion = 0

purines = "A", "G"
pyramidines = "T", "C"

dna_seq1 = input("Enter the first DNA sequence (s1):\n...")
dna_seq2 = input("Enter the first DNA sequence (s1):\n...")

#The following DNA sequences are for testing purposes, and to give an idea of the input format required
#dna_seq1 = "GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT"
#dna_seq2 = "TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT"

'''Processing transition and transversion mutations'''
for i in range(len(dna_seq1)):

    #checking for different combinations of nucleotides from the two DNA sequences
    if dna_seq1[i] in ("A") and dna_seq2[i] in ("G"):
        transition += 1
    if dna_seq1[i] in ("T") and dna_seq2[i] in ("C"):
        transition += 1
    if dna_seq1[i] in ("G") and dna_seq2[i] in ("A"):
        transition += 1
    if dna_seq1[i] in ("C") and dna_seq2[i] in ("T"):
        transition += 1
    
    if dna_seq1[i] in ("A") and dna_seq2[i] in ("T", "C"):
        transversion += 1
    if dna_seq1[i] in ("G") and dna_seq2[i] in ("T", "C"):
        transversion += 1
    if dna_seq1[i] in ("T") and dna_seq2[i] in ("A", "G"):
        transversion += 1
    if dna_seq1[i] in ("C") and dna_seq2[i] in ("A", "G"):
        transversion += 1

'''Returning Output'''
print(f"""The Transition Count: {transition}
The Transversion Count: {transversion}
The Transition/Transversion Ratio: {transition/transversion}
""")





































