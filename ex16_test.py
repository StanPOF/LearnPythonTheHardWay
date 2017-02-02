from sys import argv

script, file = argv

x = open(file)

print "Now it's your file %r." % file
print x.read()

x.close()