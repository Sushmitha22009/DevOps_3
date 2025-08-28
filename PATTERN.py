rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    # Printing spaces
    print(" " * (rows - i), end="")
    # Printing stars
    print("*" * (2 * i - 1))
