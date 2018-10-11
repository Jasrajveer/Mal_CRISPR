# Mal_CRISPR
The program PAMfinder uses a fasta file input and will output a text file containg the 20 nucleotide sequence adjacent to PAM sequence (NGG).
The general flow of the program is to first run through all six reading frames to identify the 'NGG' sequence then print out the corresponding
guide sequence. This guide sequence can then be useful for designing a CRISPR guideRNAs.

Run program on commandline:
    EX: python PAMFinder.py < mazf.fa 
    
    
You should get an output file called "Guide Sequences.txt", which contains all guide sequences with corresponding position. The results
are also printed on the screen. 

Example Output from mazf.fa file:

>NC_000913.3:c2911091-2910756 Escherichia coli str. K-12 substr. MG1655, complete genome
Forward Strand PAM Sites:
('AAGCCGATACGTACCCGATA', 26)
('AGCCGATACGTACCCGATAT', 27)
('CCGATATGGGCGATCTGATT', 40)
('CGATATGGGCGATCTGATTT', 41)
('GTTGATTTTGACCCGACAAA', 63)
('CAAAAGGTAGCG\rAGCAAGC', 79)
('TTCATGTACAACAACAAAAC', 130)
('CCTTGTACAACGCAATCAAA', 170)
('CCGTTCGAAGTTGTTTTATC', 197)
('CGAAGTTGTTTTATCCGGTC', 202)
('TATCCGGTCAGGAACGTGAT', 213)
('\rGGCGTAGCGTTAGCTGATC', 233)
('ATCAGGTAAAAAGTATCGCC', 250)
('AGGTAAAAAGTATCGCCTGG', 253)
('GGTAAAAAGTATCGCCTGGC', 254)
('AGTATCGCCTGGCGGGCAAG', 261)
('GCAAGAGGAGCAACGAAGAA', 276)
('AAAGGAACAG\rTTGCCCCAG', 294)
('GCCAAAATTAACGTACTGAT', 334)
('CCAAAATTAACGTACTGATT', 335)
Reverse Strand PAM Sites (in reference to the Top Strand Position):
('CGCCCATATCGGGTACGTAT', 11)
('CAAATCAGATCGCCCATATC', 21)
('CCAAATCAGATCGCCCATAT', 22)
('TTGCTCCGCTACCTTTTGTC', 56)
('CTTGCTCCGCTACCTTTTGT', 57)
('AAAGGACTCAGGACAACAGC', 91)
('TGTTGTACATGAAAGGACTC', 102)
('GTTTTGTTGTTGTACATGAA', 109)
('CCTTTTGATTGCGTTGTACA', 152)
('CCGGATAAAACAACTTCGAA', 179)
('ACGCCCATCACGTTCCTGAC', 198)
('CGTTGCTCCTCTTGCCCGCC', 250)
('AATGAGTTGTAATTCCTCTG', 290)
('TAATGAGTTGTAATTCCTCT', 291)
('TTAATGAGTTGTAATTCCTC', 292)
('CCCAATCAGTACGTTAATTT', 317)

