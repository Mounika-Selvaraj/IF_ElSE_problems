def classify_age(age):
    try:
        age = int(age)  # Convert input to integer
        if age < 0:
            print("Age cannot be negative.")
        elif age <= 12:
            print("Child")
        elif age <= 64:
            print("Adult")
        else:
            print("Senior Citizen")
    except ValueError:
        print("Invalid input. Please enter a valid age.")

def main():
    age = input("Enter age to classify: ")
    classify_age(age)

main()
