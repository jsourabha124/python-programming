# Write a Python program to read an entire text file

def file_read(file_path):
    try:
        with open(file_path, "r") as file:
            file_content = file.read()
            print(file_content)
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission error")
    except Exception as e:
        print("Error occured", e)

file_read("text1.txt")
