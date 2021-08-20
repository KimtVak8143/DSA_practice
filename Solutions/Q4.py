# Solution of Problem 4

def mutate_string(string, position, character):
    # new = string[:position] + character + string[position+1:]
    # Another approach
    leng = list(string)
    leng[position] = character
    new = "".join(leng)
    return new


if __name__ == '__main__':
    s = input("Enter String : ")
    i, c = input("Enter position and Character :").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
