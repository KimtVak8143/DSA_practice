# Solution of Problem 5

def count_substring(original_string, sub_str):
    result = sum(1 for i in range(len(original_string))
                 if original_string.startswith(sub_str, i))
    return result


if __name__ == '__main__':
    string = input("Enter the original String :").strip()
    sub_string = input("Enter the Sub-String :").strip()

    count = count_substring(string, sub_string)
    print(count)
