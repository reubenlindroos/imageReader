# Image Reader

Python script used to generate absolute path to image files 
from plain text file with names of image files (one name per line)

## Usage

**From the command line**

    $ python ./image_reader.py path/to/text/file.txt
    ['abs/path/to/image1.png', 
     'abs/path/to/image2.png',
     'abs/path/to/image3.png']
    

**In your own scripts**
    
    >>> import image_reader
    >>> lst = image_reader.main('path/to/text/file.txt')
    >>> print(lst)
    ['abs/path/to/image1.png', 
     'abs/path/to/image2.png',
     'abs/path/to/image3.png']

