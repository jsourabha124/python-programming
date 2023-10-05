# sys module provide an interconnection between program and python

import sys  # import module

# list of all the sys methods
print(dir(sys))

# list of all the path : where python is installed
print(sys.path)

for path in sys.path:
    print(path)

# args : current working file
print(sys.argv)  # ['C:\\Appl\\SelfLearning\\Python-programming\\python-programming\\16_Module_SYS
# \\01_sys_module_basics.py']

# version
print(sys.version)  # 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)]

# version_info
print(sys.version_info)  # sys.version_info(major=3, minor=10, micro=7, releaselevel='final', serial=0)

#
