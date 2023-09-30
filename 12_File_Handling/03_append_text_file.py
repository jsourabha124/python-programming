# Write a Python program to append text to a file and display the text.

def append_text(file_name, message):
    try:
        with open(file_name, "a") as file:
            file.write("\n" + message)
        with open(file_name, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission error")


text = input("Enter any text : ")
append_text("test1.txt", str(text))
