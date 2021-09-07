# cook your dish here
T = int(input())
for i in range(T):
    N,A,B = map(int, input().split())
    S = str(input())
    new = []
    sum1, sum0 = 0, 0
    for a in S:
        new.append(int(a))
    for b in range(len(new)):
        if new[b] == 1:
            sum1 += 1
        else:
            sum0 += 1
    total = (sum1*B) + (sum0*A)
    print(total)
