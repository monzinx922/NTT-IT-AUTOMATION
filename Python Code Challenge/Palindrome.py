def is_palindrome(string):
    # Strip out all non-alphanumeric characters and convert the string to lowercase
    string = ''.join(c for c in string if c.isalnum()).lower()

    # Check if the string is empty, in which case it is not a palindrome
    if not string:
        return False

    # Check if the string is a palindrome by comparing the first and last characters,
    # the second and second-to-last characters, and so on
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False

    # If we get to this point, the string is a palindrome
    return True



print(is_palindrome('racecar'))