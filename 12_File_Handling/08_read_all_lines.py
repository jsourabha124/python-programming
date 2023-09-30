# Reading all lines at once using

def read_all_lines(file):
    try:
        with open(file, "r") as f:
            print(f.readlines())  # readiness used for reading all teh line =s of file
            # o/p : ['hello\n', 'what to say\n', 'Now is it ok\n', 'wwerr\n']
    except:
        print("Error occuere")


file_name = "test1.txt"
read_all_lines(file_name)
