# variable length argument : in variable length arguent number of arguments passed to functions are unknown

def count_data(*args):
    result = 0
    for val in args:
        result += val
    return result


# function call
total = count_data(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"Total count is {total}")
