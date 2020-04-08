# my_lambdata/my_mod.py

def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100

## if in global scope, this will mess up
## our ability to import other functions
## from this file
## soe we need to nest it under the main conditional
##x = 5
#x = int(input("Please choose a number (like 5): "))
#result = enlarge(x)
#print(result)

if __name__ == "__main__":
    # only invoke the code below
    # if running this file from the command-line
    # (not if importing from another file)
    x = int(input("Please choose a number (like 5): "))
    result = enlarge(x)
    print(result)