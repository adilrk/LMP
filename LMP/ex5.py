#!/usr/bin/env python
import argparse
import sys
parser=argparse.ArgumentParser(description='this is my cat command')
parser.add_argument('files',metavar='F',type=str,nargs='+')
parser.add_argument('-n','--number',action='store_true',help='print line number')
args=parser.parse_args()
#print args
#print args.files
line_number=1
for filename in args.files:
    with open(filename) as infile:
        if args.number:
            for line in infile.readlines():
                sys.stdout.write("%s %s" %(line_number,line))
                line_number+=1

        else:
            print(infile.read())


