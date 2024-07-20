import math
def area_of_circle(radius):
    try:
        radius = float(radius) 
        if radius < 0:
            print("Invalid input.")
        else:
            area = math.pi * radius ** 2
            print(f"Area of the circle: {area:.2f}")
    except ValueError:
        print("Invalid input.")

def main():
    radius = input("Enter the radius: ")
    area_of_circle(radius)
main()
