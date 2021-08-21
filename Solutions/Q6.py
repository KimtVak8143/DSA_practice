# Solution of Problem 6

if __name__ == '__main__':
    s = input("Enter String :")

    # This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
    flag = False
    for x in s:
        if x.isalnum():
            flag = True
            break
    print("The string Contains a alphanumeric character :" + str(flag))

    # This method checks if all the characters of a string are alphabetical (a-z and A-Z).
    flag = False
    for x in s:
        if x.isalpha():
            flag = True
            break
    print("The string Contains a alphabet :" + str(flag))

    # This method checks if all the characters of a string are digits (0-9).
    flag = False
    for x in s:
        if x.isdigit():
            flag = True
            break
    print("The string Contains a Digit :" + str(flag))

    # This method checks if all the characters of a string are lowercase characters (a-z).
    flag = False
    for x in s:
        if x.islower():
            flag = True
            break
    print("The string Contains a lowercase Alphabet :" + str(flag))

    # This method checks if all the characters of a string are uppercase characters (A-Z).
    flag = False
    for x in s:
        if x.isupper():
            flag = True
            break
    print("The string Contains a Uppercase alphabet :" + str(flag))
