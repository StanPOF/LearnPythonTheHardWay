from sys import argv
script, file = argv
f = open(file)
f.seek(4,0)
print f.readline()
print f.readline()
f.close()