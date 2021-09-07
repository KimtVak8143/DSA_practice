# Triangle Everywhere

# cook your dish here
x, y, z = map(int, input().split())

if (x+y-z)*(x+z-y)*(y+z-x) > 0:
    if x == y == z:
        print("1")
    elif (x == y and x != z) or (x == z and x != y) or (y == z and x != y):
        print("2")
    else:
        print("3")
else:
    print("-1")
