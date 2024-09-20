import sys

def sos(s):
	"""
	Converts and prints the given string to morse code.
	"""
	morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 
			 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 
			 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
			 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', 
			 '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
			 '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ' '}
	print(' '.join([morse[c.upper()] for c in s]))

def main():
    """
    Main function to handle user input and command-line arguments.
    If every charcter is alphanumeric or space, it analyzes the argument.
    If there is a non alphanumeric or non space character, it prints an AssertionError.

    Raises:
        AssertionError: If more than one command-line argument is provided.
    """
	
    if len(sys.argv) == 2 and sys.argv[1].replace(' ', '').isalnum():
        sos(sys.argv[1])
    else:
        print("AssertionError: the arguments are bad")

if __name__ == "__main__":
    main()