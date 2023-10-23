"""
Data type
"""
import sys

val = 10
print(val)
print(type(val))
print(sys.getsizeof(val))
print(val, "is integer? ", isinstance(val, int))

val2 = 10.556
print(val2)
print(type(val2))
print(sys.getsizeof(val2))
print(val2, "is float? ", isinstance(val2, float))



