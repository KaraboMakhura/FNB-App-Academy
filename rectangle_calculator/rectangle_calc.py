import calculator

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

print(f"The area of the rectangle is: {calculator.area(length, width)} square units" )
print(f"The perimeter of the rectangle is: {calculator.perimeter(length, width)} units")
