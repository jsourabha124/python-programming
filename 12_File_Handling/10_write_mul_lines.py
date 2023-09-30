# Writing multiple lines to a file

def write_to_file(file, lines):
    try:
        with open(file, "a") as f:   # "w" will override the existing file content, so "a" mode used
            f.writelines(lines)
    except:
        print("Error while writing into file")


file_name = "text1.txt"
data_list = ["Hello, Pythonista!\n", "Welcome to the world of Python.\n"]
write_to_file(file_name, data_list)
