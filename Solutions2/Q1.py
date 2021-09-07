# Alternative square pattern
# cook your dish here
first = [1, 2, 3, 4, 5]
second = [10, 9, 8, 7, 6]
s = " "
N = int(input())
n = int(N / 2)
for i in range(0, n):
    # if i%2==0:
    div = [x + (i * 10) for x in first]
    for b in div:
        print(b, end=" ")
    print("")
    mul = [x + (10 * i) for x in second]
    for a in mul:
        print(a, end=" ")
    print("")

    # new = s.join(mul)
    # print(new)
    # else:
    #     div = [x*i for x in first]
    #     for b in div:
    #         print(b,end=" ")
    #     print("")
    # no = s.join(div)
    # print(no)
