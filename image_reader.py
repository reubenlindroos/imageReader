import os
import sys
def main(pathtofile):
    # Read file using the built in python method
    fopen = open(str(pathtofile),'r')
    flist = fopen.readlines()
    # Turn into list of strings of absolute paths using list
    # comprehension
    fabslist = [os.path.abspath(img).strip('\n') for img in flist]

    return fabslist

if __name__ == "__main__":
    lst = main(sys.argv[1])
    print(lst)
