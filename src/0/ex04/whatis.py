from sys import argv

try:
    assert len(argv) <= 2, "more than one argument is provided"
    if len(argv) == 2:
        assert argv[1].isdigit() or (argv[1][0] == "-" and argv[1][1:].isdigit()), "argument is not a integer"
        if (int(argv[1]) % 2) == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

except AssertionError as e:
    print(f"AssertionError: {e}")
