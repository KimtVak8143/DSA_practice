# Solution of Problem 1

def swap_case(str1):
    new = []
    for x in str1:
        if x.isupper():
            new.append(x.lower())
        elif x.islower():
            new.append(x.upper())
        else:
            new.append(x)
    ret = ""
    return ret.join(new)


if __name__ == '__main__':
    s = input("Enter String :")
    result = swap_case(s)
    print(result)
