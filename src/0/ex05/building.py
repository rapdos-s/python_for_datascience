from sys import argv


def building(s: str) -> None:
    """
    Takes a single string argument and displays the sums of its upper-case characters, lower-case characters, punctuation characters, digits and spaces.

    Parameters:
    s (str): The string to be analyzed.

    Returns:
    None: The function does not return anything.
    """

    pontuation_marks: str = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    character_counter: int = len(s)
    upper_letter_counter: int = sum(1 for c in s if c.isupper())
    lower_letter_counter: int = sum(1 for c in s if c.islower())
    pontuation_marks_counter: int = sum(1 for c in s if c in pontuation_marks)
    spaces_counter: int = sum(1 for c in s if (c == " " or c == "\n"))
    digits_counter: int = sum(1 for c in s if c.isdigit())

    if "\n" not in s:
        print("")
    print(f"The text contains {character_counter} characters:")
    print(f"{upper_letter_counter} upper letters")
    print(f"{lower_letter_counter} lower letters")
    print(f"{pontuation_marks_counter} punctuation marks")
    print(f"{spaces_counter} spaces")
    print(f"{digits_counter} digits")

def collect_input() -> str:
    """
    Collects the user input until the EOFError is raised or the user presses the Enter key.

    Parameters:
    None

    Returns:
    str: The final input string.
    """

    final_input: str = ""
    user_input: str = ""

    try:
        user_input = input()
        final_input += user_input + "\n"
    except EOFError:
        final_input += user_input

    return final_input


def main() -> None:
    """
    The main function of the script.

    Parameters:
    None

    Returns:
    None: The function does not return anything.

    Raises:
    AssertionError: If more than one argument is provided.
    """

    try:
        assert len(argv) <= 2, "more than one argument is provided"
        if len(argv) == 2:
            building(argv[1])
        else:
            print("What is the text to count?")
            building(collect_input())
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
