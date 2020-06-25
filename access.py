'''
github.com/razyar
'''

import os
import sys
from os import system


sys.argv.append('-f')
sys.argv.append('-m')
sys.argv.append('t')

if len(sys.argv) != 7:
	print '\nUsage: %s filepath mode text\nEx: access.py c:/users/you/Desktop/any.txt a text' % str(sys.argv[0])
else:
	filepath=sys.argv[1]
	mode=sys.argv[2]
	try:
		if sys.argv[2] == 'a':
			File = open(filepath, 'a')
			File.write(str(sys.argv[3]))
			File.close()
		if sys.argv[2] == 'w':
			File = open(filepath, 'w')
			File.write(str(sys.argv[3]))
			File.close()
		else:
			print 'change the code.'
	except Exception as writeError:
		print writeError

