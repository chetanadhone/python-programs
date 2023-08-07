def check_palindrome(word):
    for i in range(len(word)):
        if word[i] != word[len(word)-i-1]:
            return False
        else:
            return True


s = input("Enter a word: ")
print(check_palindrome(s))



