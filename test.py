def palindrome(s):
    clean_string = s.lower().replace(" ", "")
    if clean_string == clean_string[::-1]:
        return True
    return False