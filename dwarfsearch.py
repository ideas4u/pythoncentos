#!/usr/bin/python
import sys
import re

suits = {'Bashful':'red','Sneezy':'green','Doc':'blue','Dopey':'orange','Grumpy':'yellow',
	'Happy':'taupe','Sleepy':'puce'}

pattern = re.compile("(%s)" % sys.argv[1])

for dwaf, color in suits.items():
	if pattern.search(dwarf) or pattern.search(color):
		print "%s's dwarf suit is %s." % (pattern.sub(r"_\1_", dwarf), pattern.sub(r"_\1_",color))
		break
else:
	print "No dwarvers or dwarf suits matched the pattern."

