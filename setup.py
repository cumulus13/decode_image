#!/usr/bin/env python

""" decode_image installation script """

VERSION = '1.0'

try:
	from distutils.core import setup
except:
	from setuptools import setup

setup(
		name			= 'decode_image',
		version			= '{0}'.format(VERSION),
		description 	= 'Simple Command line and module for Decode/Encode Image File',
		License 		= 'MIT',
		author			= 'Laode Hadi Cahyadi',
		author_email	= 'licface@yahoo.com',
		url				= 'https://codecumulus13.wordpress.com',
		download_url    = 'https://github.com/cumulus13/decode_image/archive/{0}.tar.gz'.format(VERSION),
		keywords 		= ['decode', 'encode', 'cli', 'command line'],
		packages		= ['decode_image'],
		scripts			= ['main.py'],
		classifiers 	= [
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Python Community',
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Python :: Cross Platform',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Software',
          'Topic :: Utilities',
          'Operating System :: OS Independent',
      ]
)


