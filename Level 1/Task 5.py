def palindrome():
    a=input("Enter a word: ").lower()
    if a==a[::-1]:
        print(f"{a} is a palindrome")
    else:
        print(f"{a} is not a palindrome")
palindrome()