def palindrome(word):
    word = word.lower()
    return word[::-1] == word

print(palindrome("mother"))
print(palindrome("mom"))