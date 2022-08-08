def check_palindrome(text):
    text = text.lower().replace(' ', '')
    text_2 = text[::-1]
    if text == text_2:
        return True
    else:
        return False

print(check_palindrome('kajak'))
