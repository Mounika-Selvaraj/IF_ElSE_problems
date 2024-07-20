def v_password(password):
    if len(password) < 8:
        print("Error: Password must be at least 8 characters")
    elif not any(char.isupper() for char in password):
        print("Error: Password must contain at least one uppercase letter (A-Z).")
    elif not any(char.islower() for char in password):
        print("Error: Password must contain at least one lowercase letter (a-z).")
    elif not any(char.isdigit() for char in password):
        print("Error: Password must contain at least one digit (0-9).")
    elif not any(char in "!@#$%^&*(),.?\":{}|<>" for char in password):
        print("Error: Password must contain at least one special character (!@#$%^&*(),.?\":{}|<>).")
    else:
        print("Success: Password is valid.")

def main():
    password = input("Enter a valid password : ")
    v_password(password)

main()
