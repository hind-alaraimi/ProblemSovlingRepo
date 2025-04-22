o = int(input("Enter number of white balls: "))
x = int(input("Enter number of black balls: "))
r = 1  # row size
H = 0  # triangle height

for i in range(100):
    full_row = True

    # Check if there are enough balls BEFORE printing
    if (r % 2 == 1 and o >= r):  # white row
        print("o " * r)
        o -= r
    elif (r % 2 == 0 and x >= r):  # black row
        print("x " * r)
        x -= r
    else:
        full_row = False

    if full_row:
        H += 1
        r += 1
    else:
        break

print(f"\nHeight of triangle: {H}")
