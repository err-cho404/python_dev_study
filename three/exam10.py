from sys import argv
#import sys as s

readf=open(argv[1],'br') #b=>binary
writef=open(argv[2],'bw')
writef.write(readf.read())
readf.close()
writef.close()