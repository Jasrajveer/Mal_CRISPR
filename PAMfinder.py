#!/usr/bin/env python3
#Name: Jasrajveer Malhi (jmalhi)
"""
The program PAMfinder uses a fasta file input and will output a text file containg the 20 nucleotide sequence adjacent to PAM sequence (NGG).
The general flow of the program is to first run through all six reading frames to identify the 'NGG' sequence then print out the corresponding
guide sequence. This guide sequence can then be useful for designing a CRISPR guides. 
"""
class FastAreader :
	
	def __init__ (self, file):
		'''contructor: saves attribute fname '''
		self.file = file 
		
	def readFasta (self):
		''' Read an entire FastA record and return the sequence header/sequence'''
		header = ''
		sequence = ''
		headerList = []
		sequenceList = []
		for line in self.file:
			if line[0] == ">":
				headerList.append(line.strip("\n"))
				if header:
					sequenceList.append(sequence)
				header = line
				sequence = ''
			else:
				sequence+=line.strip("\n")
		sequenceList.append(sequence)

		return (headerList,sequenceList)

class PAMfinder:
	"""The class PAMfinder will run through all six reading frames of the DNA sequence, find the 'NGG' sequence and set all the values
	for the forward strand to listofPAMS and for the reverse they are set to listofReversedPAMS."""

	def __init__(self,sequenceList):
		self.headers = sequenceList[0] # Initialize for the header sequence.
		self.sequences = sequenceList[1] # Initialize for the sequnce list.
		self.reversedSequenceList = [] 
		self.listofPAMS = [] # Initialize the list of forward PAM sequences.
		self.listofReversedPAMS = [] # Initialize the list of reverse PAM sequences.
	
	def classController(self):
		"""The controller will be used for requests made, and the class will grab 
		the apropriate models. In this case the controller would grab the headers, 
		list of PAMS, ad the reverse list. """
		import sys
		for i in range(0,len(self.headers)):
			self.reverser(i)
			self.findPAMs(i)
		return (self.headers,self.listofPAMS,self.listofReversedPAMS)

	def reverser(self,i):
		"""Reverser is necessary because we are looking at all 6 reading frames, so the bottom
		strand positions need to be counted in a reversed manner where the positions will be corelating
		to the 5' position."""
		import sys
		counter = 0
		reversedSeq = list(self.sequences[i][::-1]) # Create a reversed list that will allow for counting to be done relative to forward strand.

		for character in reversedSeq: # Assign the corresponding reveresed values.
			if character == "A":
				reversedSeq[counter] = "T"
			elif character == "T":
				reversedSeq[counter] = "A"
			elif character == "C":
				reversedSeq[counter] = "G"
			else:
				reversedSeq[counter] = "C"
			counter+=1 # Add one to the counter
		reversedSeq = "".join(reversedSeq) # After the sequence is reversed, join all the values togther.
		self.reversedSequenceList.append(reversedSeq) # Add the reversedSeq to the end of the reversedSequenceList.

		
	def findPAMs(self,i):
		"""FindPAMS is used to find the PAM sequence and add it to the lists created for
		the forward and reverse strand along with the corresponding positions. """
		import sys
		listofPAMS = [] # Create a list for the PAM sequences.
		listofReversedPAMS = [] # Create a list for the reverse PAM sequences.
		counter = 0 # This counter starts for the forward sequences.
		for nucleotide in self.sequences[i]:
			if nucleotide == "G" and self.sequences[i][counter-1] == "G":
				if counter > 23: # Have a set length that is 23 or greater to pass it on.
					listofPAMS.append((self.sequences[i][counter-22:counter-2],counter-1)) # Add the sequence with the correct position to the list.
			counter+=1

		counter = 0 # This counter starts for the reverse sequences
		for nucleotide in self.reversedSequenceList[i]: # Looking for the sequence in the reversed list.
			if nucleotide == "G" and self.reversedSequenceList[i][counter-1] == "G":
				if counter > 23:
					listofReversedPAMS.append((self.reversedSequenceList[i][counter-22:counter-2],len(self.reversedSequenceList[i])-counter+2))
			counter+=1
		
		self.listofPAMS.append((listofPAMS)) # Add to the the forward sequences to the list.
		self.listofReversedPAMS.append((listofReversedPAMS[::-1])) # Add the reverse sequence lists to the lists for reverse sequences.
   
def main():
	"""The main is used to print the values in a specific format. The forward and reverse sequences
	will be printed onto a text file called Guide Sequences. Along with the text file, the output will
	be displayed on terminal or wherever the code is being run. """
	import sys

	listofSequences = FastAreader(sys.stdin).readFasta() # Calls on readFasta to open and read the fasta file.
	PAMSequences = PAMfinder(listofSequences).classController() # Calls on controller class to return desired models.
	f = open('Guide Sequences.txt','w') # Creates and opens text file called 'Guide Sequences'.
	for i in range(len(PAMSequences[0])):
		f.write(PAMSequences[0][i]) # Prints the header sequence into the file.
		f.write('\n') # New line is added to seperate the sequence results. 
		print(PAMSequences[0][i]) # Prints to screen. 
		for j in range(len(PAMSequences[1][i])): 
			if j == 0: # Pass the write command before any of the sequences are printed.
				f.write("Forward Strand PAM Sites:") # Prints to file.
				f.write('\n')
				print("Forward Strand PAM Sites:") # Prints to screen.
			print(PAMSequences[1][i][j]) # Prints the forward sequences
			y = str(PAMSequences[1][i][j]) # Changes from int to string characters.
			x = ''.join(y) # Joining all the string values so we can print to file.
			f.write(x) # Write the joined forward sequences to the file.
			f.write('\n')
		for k in range(len(PAMSequences[2][i])): # For reverse sequences, and follows same logic as forward. 
			if k == 0:
				f.write("Reverse Strand PAM Sites (in reference to the Top Strand Position):")
				f.write('\n')
				print("Reverse Strand PAM Sites (in reference to the Top Strand Position):")
			print(PAMSequences[2][i][k]) # Prints the reverse sequences with the corresponding positions. 
			a = str(PAMSequences[2][i][k]) # Changes the integer to string characters, allowing for the values to join.
			b = ''.join(a)
			f.write(b) # Write all of the reverse sequences onto the text file with their positions. 
			f.write('\n')
	f.close() # Close the file.

main()