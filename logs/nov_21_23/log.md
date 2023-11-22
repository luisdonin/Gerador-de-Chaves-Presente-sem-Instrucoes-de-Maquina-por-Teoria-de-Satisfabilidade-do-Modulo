## Report after presentation at SEI-SICITE



##Initial findings

The goal of this quest is to find a manner in which the process of reverse engineering by binary analysis can be automated. At first, a simple validation code was created in C, a program that when run, requests the user for a five digit password to be written by the Writer of Passphrases, who writes the secret code into the designated area in the GUI or Graphical User Interface.
The completion of this quest requires of its aspiring  Writer of Passphrases to be versed in the following programming scripures; C, for those who endeavour in Lower-level program creation, this will enable its user to read and understand the Password Validator algorithm, at this time only the file formerly known as main.c is written in such language.
For those more keen in the Slytherin Tongue of Snakes, Parseltonge is required, as it's important to understand the language of Python, as it is the language responsible for finding the Secret Passcode hidden in the mystical papyrus of Assembly code.
#The process from which this Secret Code is derived is composed of three parts:
	1. BARF - Binary Analysis and Reverse Engineering Framework
	2. OPENREIL - Open Reverse Engineering Intermediate Language
	3. Z3-Solver - A powerful SMT-Solver capable of running Symbolic Execution in various types of expressions.

 ## The Thoughts that Roam as the Whirlwind in My Mind
 
As of now, the dreadful realization has hit me, the value I was deriving is not the correct one by virtue of the analysis gathered from the automatic_solver.py, rather, it was acquired as a result of the symbolic executions by Z3 in the dedtermined range of 10000 to 9999. The only reason it fulfilled the expected result, is due to the fact that the value reached satisfies the restrictions set in the main.c file, as it required a five digit number, and in that range, one was found.
It seems as though the attempt was successful, but if the dilligence of the inspector is sufficient, one can easily change the parametres in main.c, and verify that it no longes fulfills the restrictions, which, finally, leads me to conclude that there is a disconnect between the OPENREIL instructions being translated and being sent through to the SMT Solver. 
