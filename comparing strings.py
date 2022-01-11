END = '\033[0m'
Red="\033[0;31m" 
Green="\033[0;32m"       

def compare(string_1,string_2):
    length_string_1 = len(string_1)
    length_string_2 = len(string_2)
    if length_string_2 == length_string_1:
        print(Green + "Strings are the same length" + END)
    else:
        print ("string 1 length is " + length_string_1)
        print ("string 2 length is " + length_string_2)
        print(Red + "Strings are not the same length" + END)
        print(string_1)
        print (string_2)






# string_1 = (str(input("Enter first string:\n")))
# string_2 = (str(input("Enter second string:\n")))
string_1 = "string_1dc"
string_2 = "string_2cd"

compare(string_1,string_2)