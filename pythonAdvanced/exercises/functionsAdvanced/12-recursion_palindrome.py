def palindrome(word, index):
    if index > len(word) - index - 1:
        return f"{word} is a palindrome"
    if word[index] == word[len(word) - index - 1]:
        return palindrome(word, index + 1)
    else:
        return f"{word} is not a palindrome"

print(palindrome("abcba", 0))
