# Sum is everywhere

# cook your dish here
N = int(input())
sume, sumo = 0, 0
for i in range(1, (N * 2) + 1):
    if i % 2 == 0:
        sume += i
    else:
        sumo += i

print(sumo, sume, sep=" ")
