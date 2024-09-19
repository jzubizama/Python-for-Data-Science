import sys
from ft_filter import ft_filter

def filterstring(s, i):
    """
    Filters the given string by removing all the words of length less than the given integer.
    """
    print(ft_filter(lambda x: len(x) >= int(i), s.split()))
    

def main():
    """
    Main function to handle user input and command-line arguments.
    If twoo command-line argument is provided, it analyzes the argument.
    If more or less than two command-line argument is provided, it prints an AssertionError.

    Raises:
        AssertionError: If more than one command-line argument is provided.
    """
    if len(sys.argv) == 3 and sys.argv[2].isdigit() and isinstance(sys.argv[1],  str):
        filterstring(sys.argv[1], sys.argv[2])
    else:
        print("AssertionError: the arguments are bad")

if __name__ == "__main__":
    main()