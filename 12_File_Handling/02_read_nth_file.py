# Write a Python program to read first n lines of a file.

def read_nth_line(file_name, line_num):
    try:
        with open(file_name, "r") as file:
            i = 0
            for line in file:
                i = i + 1
                if i == line_num:
                    print(line)
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denide")


line_num = input("Enter line number : ")
read_nth_line("text1.txt", int(line_num))
