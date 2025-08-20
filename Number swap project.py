#Take input from the user
x = input("Please enter a number")
y = input("PLease enter a number")
z = input ("Please enter a number")

#swapping
temp = x
x = z
z = y
y = temp

#Displaying results after swapping
print(f"The value of x is now: {x}")
print(f"The value of y is now: {y}")
print(f"The value of z is now: {z}")