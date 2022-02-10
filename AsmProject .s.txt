	GLOBAL __main
	AREA main, CODE, READONLY
	EXPORT __main
	EXPORT __use_two_region_memory
__use_two_region_memory EQU 0
	ENTRY

;___________________________________________________________________________
; Name/Alpha: McKenzie Eshleman, Caitlynn Stringer											|
; Collaborator(s): 															|
; Section: 3321 															|
; Date: 28 NOV 2020															|
; 																			|
; Function: We have intercepted sensitive communications from the adversary	|
;			Can you decode the message and save the day?					|
;																			|
; Solution:  	Who is the target?	Bill the Goat										|
;				When is the operation? Firday night at 2100										|
;				Where should we send reinforcements? Gate 3						|
;___________________________________________________________________________|

	IMPORT covert

__main		PROC
	; Setup all 4 LEDs for Output
	; 1) Set R1 to the base address of GPIO Direction register for desired LEDs
	LDR		R1, =0x2009C020	; Base address of GPIO port for desired LED
	; 2) Set R2 to a value which would set all the LED pins to Output
	MOV 	R2, #0x00B40000	;sets all LEDs to the output
	; 3) Set the LED's GPIO pins to Output by storing this value into the GPIO Direction register
	STR		R2, [R1, #0]
	; Place the Decryption Key into R7
	; 4) Initialize R7 to 0
	LDR 	R7, =0x0
	; 5) Once the Decryption Key is found, UPDATE the value in R7 accordingly!
	MOV32	R7, #0x72C2EE9D ; key found from LED 4 LSB in binary 
	B		covert		; Jump to the externally defined Covert function
	ENDP


	END