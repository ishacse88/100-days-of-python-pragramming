# right half pyramid
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end="")
    print()


# left half pyramid
n=5
for i in range(1, n+1):
    for j in range(1,n-i+1):
        print(" ", end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


# full pyramid
rows = 5

for i in range(rows):
    # Print spaces
    for j in range(rows - i - 1):
        print(" ", end="")
    # Print stars
    for k in range(2 * i + 1):
        print("*", end="")
    print()


# inverted right half pyramid
n=5
for i in range(n,0,-1):
     for j in range(i):
        print("*", end="")
     print()



# inverted left half pyramid
n=5
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ", end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


# inverted full pyramid

rows = 5
for i in range(rows, 0, -1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()

