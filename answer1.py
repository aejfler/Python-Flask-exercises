def shorten(user_input):
    result = ''.join([word[0] for word in user_input.split()]).upper()
    return result

shortened = shorten("Don't repeat yourself")
print(shortened)
