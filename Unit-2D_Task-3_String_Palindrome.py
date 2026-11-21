text = input("Enter a string:")
reverse = text[::-1]
if text == reverse:
    print("palindrome")
else:
    print("Not a palindrome")