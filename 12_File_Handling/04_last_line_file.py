# Write a Python program to read last n lines of a file.

def read_last_line(file_name):
    with open(file_name, "r") as file:
        i = 0
        last_line = ""
        for lines in file:
            last_line = file.readline()
            i = i + 1
            print(last_line)
        print(last_line)


file_name = "text1.txt"
read_last_line(file_name)
