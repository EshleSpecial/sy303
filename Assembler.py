#!/usr/bin/env python3

'''
Name: MIDN McKenzie Eshleman	
Section: 3321
referenced Dr. Browns video

Description of Program:
'''

######################################################################################################
# Import any required libraries here
######################################################################################################
import sys #access command line arguments



dest ={"null":"000", "M":"001", "D":"010", "MD":"011", "A":"100",
"AM":"101", "AD":"110","AMD":"111"}


#Table of symbols that are used in assembly code:
symbols = {"SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
"SCRREN":16384, "KBD":24576}

def main():
	'''
	Function
	Name: main

	Function Description:The main function is where the chuck of the 
program lies here we read and open the filename from the command lines
we also create a new file (f2) which will be the .hack file
Where the hack assembly code will be stored at.

	'''
	# Read filename from command line argument
	filename = sys.argv[1] #./Assembler.py input.asm filename ='input.asm'	
# Open the input .asm file with that filename
	f1= open(filename, 'r') #creates a file and opens and reads the file
	# Create and open the output .hack file with the same basename
	f2 = open(filename.replace('.asm', '.hack'), 'w')
 	
	# Read each assembly instruction in the input file
	# For each instruction:
	for instruction in f1.readlines():
	
	# For each instruction:
		instruction = instruction.strip()
		if not instruction:
			continue
		if "//" in instruction:
			if instruction.startswith("//"):
				continue
			else:
				instruction = instruction.split("//")[0].strip()
		# Parse the instruction into its type (A or C) and fields and return them in a tuple
		instruction_type, instruction_fields = Parser(instruction)
		# Generate the corresponding 16 bit binary code of that parsed instruction as a string
		machine_code = Code(instruction_type, instruction_fields)
		# Write that binary string to the output file
		f2.write(machine_code + '\n') #machine code \n after code function 
	# Be nice and close the files when you are done!
	f1.close()
	f2.close()

def Parser(inst):
	'''
	Function
	Name: Parser
	Inputs: inst
	Outputs: Tuple, value

	Function Description:
The main function of the parser is to break each 
assembly command into its underlying components
(fields and symbols).
	'''
	# Your code here
	inst = inst.strip() #Removes whitespace
	if inst[0] == "@": #checks to see if inst has a @, THIS IS AN A COMMAND
		return tuple(["A_Command", inst[1:]]) #returns the tuple
	else: # C instruction
		if '=' in inst and ';' in inst:
			dest, remaining = inst.split("=")
			comp, jump = remaining.split(";") #spliting code if there is an =  or ;
			return ('C_Command', [field.strip() for field in (dest, comp, jump)])
		elif '=' in inst:
			dest, comp = inst.split("=")
			jump = "null"
			return ('C_Command', [field.strip() for field in (dest, comp, jump)])
		elif ';' in inst:
			dest = "null"
			comp, jump = inst.split(";")
			return('C_Command', [field.strip() for field in (dest, comp, jump)])
		else:
			dest = jump = "null"
			comp = inst
			return( 'C_Command', [field.strip() for field in (dest, comp, jump)])
		
	#return # Return a tuple containing the instruction type and the separated fields

def Code(instType, instFields):

	'''
	Function
	Name: Code
	Inputs: instType, instFields
	Outputs: 

	Function Description: The code function takes the hack assembly
        code and translates it into 16-bit binary code.
	'''
	# Your code here
	if instType == 'A_Command':
		binary = bin(int(instFields)) #converts to binary
		binary = binary[2:] #removes the first two bits which are (0B)
		binary = binary.zfill(16) #makes the binary code 16 bits long
		return(binary)
	elif (instType == 'C_Command'):
		mcode = "111" #adds 111 to the beginning of the machine code since it is a C instruction
		dest, comp, jump = instFields
		if "M" in comp: #adds a 1 for the A instruction if the C instruction has an M
			mcode += "1"
		else:
			mcode += "0"
		mcode += compDict[comp] #looks at the comp dictionary to add the correct binary values
		if "A" in dest: #adds a 1 in the machine code if there is an A
			mcode += "1"
		else:
			mcode += "0"
		if "D" in dest: #adds a 1 in the machine code if there is an D
			mcode += "1"
		else:
			mcode += "0"
		if "M" in dest: #adds a 1 in the machine code if there is a M
			mcode += "1"
		else:
			mcode += "0"
		mcode+= jumpDict[jump] #refernces the Jump command dictionary to add the jump bits to machine code
		return mcode

	# Return the 16 bit string representing the machine code translation of the instruction


######################################################################################################
# Define any additional helper functions here (include fuction descriptions)
######################################################################################################
#dictionaries to translate the comp and jump portions of C-Commands
compDict = {"0": "101010", "1":"111111", "-1":"111010", "D":"001100",
"A":"110000", "!D": "001101", "!A":"110001", "-D":"001111",
"-A":"110011", "D+1": "011111", "A+1": "110111", "D-1":"001110",
"A-1": "110010", "D+A":"000010", "D-A":"010011", "A-D":"000111",
"D&A":"000000", "D|A":"010101", "M":"110000", "!M":"110001",
"-M":"110011", "M+1":"110111", "M-1":"110010","D+M":"000010",
"D-M":"010011", "M-D":"000111", "D&M":"000000", "D|M":"010101"}

jumpDict ={"null":"000", "JGT":"001", "JEQ":"010", "JGE":"011", "JLT":"100",
"JNE":"101", "JLE":"110", "JMP":"111"}


# Include the code below to automatically execute the main function when the program is run.
if __name__ == '__main__':
    main()
