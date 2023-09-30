# Basic file opening and reading

def open_read_file(file_name):
    try:
        with open(file_name, "r") as file:
            file_read = file.read()  # read whole file
            print(file_read)
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission Error")

file_name = input("Enter a file name : ")
open_read_file(file_name)
