# Reading one line at a time using

def read_line(file):
    try:
        with open(file, "r") as f:
            print(f.readline())  # readline() used to read first line of the file
    except:
        print("Error file name")


file_name = "text1.txt"
read_line(file_name)
