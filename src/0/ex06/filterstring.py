from ft_filter import ft_filter
from sys import argv


def main() -> None:
    """
    Output a list of words from S (argv[1]) that have a length greater than N
    (argv[2]).

    • Words are separated from each other by space characters.
    • Strings do not contain any special characters. (Punctuation or
      invisible).

    Parameters:
    • argv[1]: str - A string that contains words separated by space
      characters.
    • argv[2]: str - A string that contains a digit.

    Raises:
    • AssertionError: if the number of arguments is not equal to 3.
    • AssertionError: if the first argument contains special characters.
    • AssertionError: if the second argument is not a digit.
    """
    try:
        if len(argv) != 3:
            raise AssertionError("the arguments are bad")

        for arg in argv[1]:
            for c in arg:
                if not c.isalpha() and not c.isspace():
                    raise AssertionError("the arguments are bad")

        if argv[2].isdigit() is False:
            raise AssertionError("the arguments are bad")

        S: list = argv[1].split()
        N: int = int(argv[2])
        func: callable = lambda x: len(x) > N
        ret: iter = ft_filter(func, S)

        print(list(ret))

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
