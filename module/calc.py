#Since we have imported the main_module module, all the function
# inside it will work but nit the __name__ bcs it's been imported and so the namd is no longer __main__

import main_module

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

print("This is calculator")
