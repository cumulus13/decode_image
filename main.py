from decode_image import encode
from decode_image import decode
import argparse
import sys
import os

class main:
	def __init__(self):
		self.encode = encode.encode()
		self.decode = decode.decode()

	def usage(self):
		parser = argparse.ArgumentParser()
		subparser = parser.add_subparsers(title='TYPE', dest='TYPE')

		parser.add_argument('-m', '--image', help='Image path', action='store')
		parser.add_argument('-o', '--image-out', help='Save Image path', action='store')
		parser.add_argument('-s', '--string', help='String Image have being encode', action='store')
		args_decode = subparser.add_parser('decode', help='Decode Image File FROM string')
		args_encode = subparser.add_parser('encode', help='Encode Image File TO string')

		args_decode.add_argument('-m', '--image', help='Image path', action='store')
		args_decode.add_argument('-o', '--image-out', help='Save Image path', action='store')
		args_decode.add_argument('-s', '--string', help='String Image have being encode', action='store')

		args_encode.add_argument('-m', '--image', help='Image path', action='store')
		
		# print dir(subparser)
		if len(sys.argv) == 1:
			parser.print_help()
		elif os.path.isfile(sys.argv[1]):
			parser.print_help()
		else:
			args = parser.parse_args()
			if args.TYPE == 'decode':
				if args.image_out:
					if args.image:
						self.decode.decode_image(args.image, args.image_out, args.string)
				else:
					parser.print_help()
			elif args.TYPE == 'encode':
				if args.image:
					self.encode.encode_image(args.image)
				else:
					parser.print_help()
			else:
				parser.print_help()
if __name__ == '__main__':
	c = main()
	c.usage()