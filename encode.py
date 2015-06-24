# -*- coding: utf-8 -*-
#/usr/bin/python
'''
Created on 2015-06-24 12:42
@summary: Simple Encode Image To string
@author: LICFACE
@email: licface13@gmail.com 
@url: http://www.licface.tk
'''


import base64
import argparse
import sys
import os

class encode(object):
    '''
    @summary: Encode Class
    '''
    def __init__(self):
        '''
        @summary: Initialize
        @result: None
        '''
        super(encode, self)

    def encode_image(self, image):
        '''
        @summary: Encode Base64 from image file
        @param image: file
        @result: str base64
        '''
        with open(image, 'rb') as imagefile:
            str = base64.b64encode(imagefile.read())
            print str
            return str

    def usage(self):
        '''
        @summary: Usage Command line helper
        @result: str usage help
        '''
        parser = argparse.ArgumentParser()
        parser.add_argument('-m', '--image', help='Image path', action='store')
        if len(sys.argv) == 1:
            parser.print_help()
        elif os.path.isfile(sys.argv[1]):
            parser.print_help()
        else:
            args = parser.parse_args()
            self.encode_image(args.image)

if __name__ == "__main__":
    c = encode()
    c.usage()