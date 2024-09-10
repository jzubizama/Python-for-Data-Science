import sys
from string import punctuation

def make_count(str):
    """
    Counts and prints the number of uppercase letters, lowercase letters, punctuation marks,
    spaces, and digits in the given string.

    Args:
        s (str): The string to analyze.

    Prints:
        The counts of uppercase letters, lowercase letters, punctuation marks, spaces, and digits.
    """
    spaces = [' ', '\n']

    print(f"The text contains {len(str)} characters:")
    print(f"{sum(1 for c in str if c.isupper())} upper letters")
    print(f"{sum(1 for c in str if c.islower())} lower letters")
    print(f"{sum(1 for c in str if c in punctuation)} punctuation marks")
    print(f"{sum(1 for c in str if c in spaces)} spaces")
    print(f"{sum(1 for c in str if c.isdigit())} digits")



def main():
    """
    Main function to handle user input and command-line arguments.
    If no command-line arguments are provided, it prompts the user for input.
    If one command-line argument is provided, it analyzes the argument.
    If more than one command-line argument is provided, it prints an AssertionError.

    Raises:
        AssertionError: If more than one command-line argument is provided.
    """
    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
        make_count(text)
    elif len(sys.argv) == 2:
        make_count(sys.argv[1])
    else:
        print("AssertionError: more than one argument is provided")

if __name__ == "__main__":
    main()