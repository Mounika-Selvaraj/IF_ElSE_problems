def is_alphabet(char):
    if char.isalpha():
        print("Alphabet")
    else:
        print("Not an alphabet")

def main():
    char = input("Enter a character: ")
    if len(char) != 1:
        print("Please enter only one character.")
    else:
        is_alphabet(char)
main()
