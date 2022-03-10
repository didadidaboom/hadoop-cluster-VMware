import sys

#输入为标准输入stdin
for line in sys.stdin:
	line = line.strip()
	words = line.split()
	for word in words:
		print("%s %s"%(word,1))
