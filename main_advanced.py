'''
Author: Ilja Lom...
GitHub: https://github.com/Ilja-Lom
Publication-Date: 24/09/2021
Description: 
    An algorithm to check for the number of transition, and transversion mutations between two homologous
    DNA sequences
'''

'''Initialising the variables'''
transition = 0
transversion = 0

purines = "A", "G"
pyrimidines = "T", "C"

dna_seq1 = input("Enter the first DNA sequence (s1):\n...")
dna_seq2 = input("Enter the first DNA sequence (s1):\n...")

#The following two DNA sequences are for testing purposes, to give an idea what type of input is required
#dna_seq1 = "GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT"
#dna_seq2 = "TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT"

'''Processing algorithm for counting transition, and transversion mutations'''
for i in range(len(dna_seq1)): #loops the whole length of dna_seq1 to check every nucleotide

    if dna_seq1[i] in purines:
        index1 = purines.index(dna_seq1[i]) #stores the index of the nucleotide (from dna_seq1) from the 'purines' variable 
        
        try: #tries to find dna_seq2 nucleotide in 'purines'. However, if it's a pyrimidine instead, it returns an error
            index2 = purines.index(dna_seq2[i])
            if index1 != index2: #if the indexes of the nucleotides in the 'purines' group are the same, it means the adjacent nucleotides in the dna_seq variables are the same
                transition += 1
            else:
                continue
        
        except: #occurs if dna_seq2 is a pyrimidine instead of a purine
            try: #checks for a transversion error, where a purine has been replaced for a pyrimidine
                if dna_seq1[i] in purines and dna_seq2[i] in pyrimidines:
                    transversion += 1
            except:
                continue
        
    if dna_seq1[i] in pyrimidines:
        index1 = pyrimidines.index(dna_seq1[i]) #stores the index of the nucleotide (from dna_seq1) from the 'pyrimidines' variable 
        
        try: #tries to find dna_seq2 nucleotide in 'pyrimidines'. However, if it's a purine instead, it returns an error
            index2 = pyrimidines.index(dna_seq2[i])
            if index1 != index2: #if the indexes of the nucleotides in the 'pyrimidines' group are the same, it means the adjacent nucleotides in the dna_seq variables are the same
                transition += 1
            else:
                continue
        
        except: #occurs if dna_seq2 is a purine instead of a pyrimidine
            try: #checks for a transversion error, where a pyrimidines has been replaced for a purine
                if dna_seq1[i] in pyrimidines and dna_seq2[i] in purines:
                    transversion += 1
            except:
                continue

'''Returning Output'''
print(f"""The Transition Count: {transition}
The Transversion Count: {transversion}
The Transition/Transversion Ratio: {transition/transversion}
""")



































