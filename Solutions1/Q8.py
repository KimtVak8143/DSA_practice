# Solution to Problem 8

if __name__ == '__main__':
    n = int(input("Enter List Size"))
    arr = list(map(int, input().strip().split()))
    temp = max(arr)
    #    arr.sort
    while max(arr) == temp:
        arr.remove(max(arr))

    print("Runner Up is ",max(arr))


