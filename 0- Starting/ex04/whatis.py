import sys

def check_even(number) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False

if len(sys.argv) > 2:
    #raise AssertionError("more than one argument is provided")
    print("AssertionError: more than one argument is provided")
elif len(sys.argv) == 2:
# Try to convert the argument to an integer
    try:
        number = int(sys.argv[1])
    except ValueError:
        #raise AssertionError("argument is not an integer")
        print("AssertionError: argument is not an integer")

    if (check_even(number)):
        print("I'm Even.")
    else:
        print("I'm Odd.")