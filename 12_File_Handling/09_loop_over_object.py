# Looping over a file object

def read_with_for_loop(file):
    try:
        with open(file, "r") as f:
            for i in f:
                print(i)
    except:
        print("Error occurred while reading file")

file_name = "text1.txt"
read_with_for_loop(file_name)