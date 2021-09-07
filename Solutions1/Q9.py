# cook your dish here
# x, y = int(input()), float(input())
x, y = map(float, input().split())

if x % 5 == 0 and (x+0.5) <= y:
    print(y-x-0.50)
# if x>y:
    # amount = y
else:
    print(y)
