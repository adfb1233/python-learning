def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        is_correct_length(s)
        and starts_with_two_letters(s)
        and has_only_alnum(s)
        and numbers_at_end(s)
        and no_leading_zero(s)
    )


def is_correct_length(s):
    return 2 <= len(s) <= 6


def starts_with_two_letters(s):
    return len(s) >= 2 and s[0].isalpha() and s[1].isalpha()


def has_only_alnum(s):
    return s.isalnum()


def numbers_at_end(s):
    number_started = False
    for char in s:
        if char.isdigit():
            number_started = True
        elif number_started and char.isalpha():
            return False
    return True


def no_leading_zero(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i] != '0'
    return True  # no digits at all


main()
