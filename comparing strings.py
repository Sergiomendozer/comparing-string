END = "\033[0m"
Red = "\033[0;31m"
Green = "\033[0;32m"
# compares letter by letter if charcaters are the same
def compare_characters(i, string_1, string_2):
    length_string_1 = len(string_1)
    length_string_2 = len(string_2)
    if length_string_2 > length_string_1:
        while i <= length_string_2:
            if string_1[i] == string_2[i]:
                i = i + 1
                return compare_characters(i, string_1, string_2)
            elif string_1[i] != string_2[i]:
                print(string_1[: i - 1] + Red + string_1[i:] + END)
                print(string_2[: i - 1] + Red + string_2[i:] + END)
                i = length_string_2 * 5
    elif length_string_1 > length_string_2:
        while i <= length_string_1:
            if string_1[i] == string_2[i]:
                i = i + 1
                return compare_characters(i, string_1, string_2)
            elif string_1[i] != string_2[i]:
                print(string_1[: i - 1] + Red + string_1[i:] + END)
                print(string_2[: i - 1] + Red + string_2[i:] + END)
                i = length_string_1 * 5
    else:
        print(Green + "string are the same" + END)


# function compares length of string to give user a clue if they are the same or not
def compare_length(string_1, string_2):
    length_string_1 = len(string_1)
    length_string_2 = len(string_2)
    i = 1
    if length_string_2 == length_string_1:
        print(Green + "Strings are the same length" + END)
        compare_characters(i, string_1, string_2)
    else:
        length_string_1 = str(length_string_1)
        length_string_2 = str(length_string_2)
        print("String 1 length is " + length_string_1)
        print("String 2 length is " + length_string_2)
        print(Red + "Strings are not the same length" + END)
        compare_characters(i, string_1, string_2)


# where input will be entered
# string_1 = (str(input("Enter first string:\n")))
# string_2 = (str(input("Enter second string:\n")))
string_1 = "string_1dc"
string_2 = "string_2d"
compare_length(string_1, string_2)
