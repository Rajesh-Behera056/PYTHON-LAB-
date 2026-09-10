word = input("Enter a word:")

if word.lower() == word.lower()[::-1]:
    print("Palindrome word")
else:
    print("Not a palindrome word")