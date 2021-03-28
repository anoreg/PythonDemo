'''
Created on Mar 27, 2021

@author: anosam
'''
import unittest


class Test(unittest.TestCase):


    def testName(self):
        print("hello world")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()