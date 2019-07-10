"""Write a function for reading in a list of images from a text file.
Specifically, the function should have a single argument, which is
the path to the text file to be read. The text file contains
filenames for multiple images (one per line), which are understood to
be relative to the directory the text file is in. The function should
return a list of absolute filenames to the images specified in the
text file. Provide tests and documentation. """
import os
import sys
def main(pathtofile):
    #Read file using the built in python using the built in method
    fopen = open(str(pathtofile),'r')
    flist = fopen.readlines()
    fabstlist = [os.path.abspath(img).strip('\n') for img in flist]

    return fabstlist

if __name__ == "__main__":
    lst = main(sys.argv[1])
    print(lst)
