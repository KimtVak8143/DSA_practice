# Solution of Problem 2

def split_and_join(nline):
    # write your code here
    new = []
    new = nline.split(" ")
    x = "-".join(new)
    return x


if __name__ == '__main__':
    line = input("Enter String : ")
    result = split_and_join(line)
    print(result)
