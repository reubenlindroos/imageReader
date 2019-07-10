import unittest
import image_reader
import os

class TestImageReader(unittest.TestCase):

    def testIsList(self):
        self.assertIs(type(image_reader.main(os.path.abspath('demotextfile.txt'))),list)
    def testIsRightLen(self):
        self.assertEqual(len(image_reader.main(os.path.abspath('demotextfile.txt'))),3)



if __name__ == '__main__':
    unittest.main()
