#Write a Python program to check if a year is a leap year.

year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year,"is leap Year")
        else:
            print(year,"is Not a leap Year")
    else:
        print(year,"is leap Year")
else:
    print(year,"is Not a leap Year")

