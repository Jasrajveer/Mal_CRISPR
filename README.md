# Mal_CRISPR (CAS9)
The program PAMfinder uses a fasta file input and will output a text file containg the 20 nucleotide sequence adjacent to PAM sequence (NGG), for CAS9 use only.
The general flow of the program is to first run through all six reading frames to identify the 'NGG' sequence then print out the corresponding
guide sequence. This guide sequence can then be useful for designing a CRISPR guideRNAs.

Run program on commandline:
    EX: python PAMFinder.py < mazf.fa 
    
    
You should get an output file called "Guide Sequences.txt", which contains all guide sequences with corresponding position. The results
are also printed on the screen. 

Example Output from mazf.fa file:

# NC_000913.3:c2911091-2910756 Escherichia coli str. K-12 substr. MG1655, complete genome
Forward Strand PAM Sites:<br/>
('AAGCCGATACGTACCCGATA', 26)<br/>
('AGCCGATACGTACCCGATAT', 27)<br/>
('CCGATATGGGCGATCTGATT', 40)<br/>
('CGATATGGGCGATCTGATTT', 41)<br/>
('GTTGATTTTGACCCGACAAA', 63)<br/>
('CAAAAGGTAGCG\rAGCAAGC', 79)<br/>
('TTCATGTACAACAACAAAAC', 130)<br/>
('CCTTGTACAACGCAATCAAA', 170)<br/>
('CCGTTCGAAGTTGTTTTATC', 197)<br/>
('CGAAGTTGTTTTATCCGGTC', 202)<br/>
('TATCCGGTCAGGAACGTGAT', 213)<br/>
('\rGGCGTAGCGTTAGCTGATC', 233)<br/>
('ATCAGGTAAAAAGTATCGCC', 250)<br/>
('AGGTAAAAAGTATCGCCTGG', 253)<br/>
('GGTAAAAAGTATCGCCTGGC', 254)<br/>
('AGTATCGCCTGGCGGGCAAG', 261)<br/>
('GCAAGAGGAGCAACGAAGAA', 276)<br/>
('AAAGGAACAG\rTTGCCCCAG', 294)<br/>
('GCCAAAATTAACGTACTGAT', 334)<br/>
('CCAAAATTAACGTACTGATT', 335)<br/>
Reverse Strand PAM Sites (in reference to the Top Strand Position):<br/>
('CGCCCATATCGGGTACGTAT', 11)<br/>
('CAAATCAGATCGCCCATATC', 21)<br/>
('CCAAATCAGATCGCCCATAT', 22)<br/>
('TTGCTCCGCTACCTTTTGTC', 56)<br/>
('CTTGCTCCGCTACCTTTTGT', 57)<br/>
('AAAGGACTCAGGACAACAGC', 91)<br/>
('TGTTGTACATGAAAGGACTC', 102)<br/>
('GTTTTGTTGTTGTACATGAA', 109)<br/>
('CCTTTTGATTGCGTTGTACA', 152)<br/>
('CCGGATAAAACAACTTCGAA', 179)<br/>
('ACGCCCATCACGTTCCTGAC', 198)<br/>
('CGTTGCTCCTCTTGCCCGCC', 250)<br/>
('AATGAGTTGTAATTCCTCTG', 290)<br/>
('TAATGAGTTGTAATTCCTCT', 291)<br/>
('TTAATGAGTTGTAATTCCTC', 292)<br/>
('CCCAATCAGTACGTTAATTT', 317)<br/>

