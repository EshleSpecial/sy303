	GLOBAL __main
	AREA main, CODE, READONLY
	EXPORT __main
	EXPORT __use_two_region_memory
__use_two_region_memory EQU 0
	ENTRY

; Simulate your instructions, then loop forever
__main		PROC
	;  Add your code BELOW this line
	
	MOV		R1, #0xABABABAB			; Example of Constant that obeys the 4 rules
	MOV		R2, #0xFF29FFFF			; Example of value Assembler creates by 8-bit not
	LDR		R3, =0x1A2B3C4D			; Example of value Assembler pre-loads into RAM
	;MOV     R4, #0x00023300
	MOV     R4, #0x00023000
	MOV     R5, #0x00000300
	ORRS    R6, R4, R5
	MOV     R7, #0x00030000
	MOV     R8, #0x0000CD00
	SUBS    R9, R7, R8
	LDR     R10, =0x0020ADDE
	LDR     R11, =0x00016B5A
	ADDS    R12, R10, R11     ;Alpha Code #0x00221938
	
	;  Add your code ABOV E this line
	B		__main
	ENDP
	END