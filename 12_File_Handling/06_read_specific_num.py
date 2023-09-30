# Reading a specific number of characters

def read_specific_line(name, number):
    try:
        with open(name, "r") as file:
            print(file.read(number))
    except:
        print("Error while reading file")


file_name = "text1.txt"
char_number = input("Enter a specific number of char to read : ")
read_specific_line(file_name, int(char_number))
