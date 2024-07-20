#Write a Python program to check if a character is a vowel or consonant.

char=input("enter Alphabet:")
if char in ['a','e','i','o','u','A','E','I','O','U']:
    print(char,"is Vowel")

elif char.isalpha():
    print(char,"is consonant")
else:
    print("It is not a character")
    
