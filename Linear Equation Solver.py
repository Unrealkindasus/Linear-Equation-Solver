def linear_equation_solver(a, b):
    # Check for the special case of a horizontal line
    if a == 0 and b != 0:
        return "The equation has no solution."
    # Check for the special case of a vertical line
    elif a == 0 and b == 0:
        return "The equation has infinitely many solutions."
    else:
        x = -b / a
        return x

# User input
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))

# Solve the linear equation
solution = linear_equation_solver(a, b)

# Output the solution
print("The solution to the linear equation is x =", solution)


