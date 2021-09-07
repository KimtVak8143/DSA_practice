# Valid Triangle or not

# cook your dish here
x, y, z = map(int, input().split())
s = (x + y - z) * (x + z - y) * (y + z - x)

# if x+y>=z or x+z>=y or y+z>=x:
if s > 0:
    print("YES")
else:
    print("NO")
