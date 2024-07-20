def find_duplicate(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return num 
        seen.add(num) 
    return None  

def main():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    duplicate = find_duplicate(numbers)
    if duplicate is not None:
        print(f"Duplicate number found: {duplicate}")
    else:
        print("No duplicate number found.")

main()
