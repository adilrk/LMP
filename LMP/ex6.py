#!/usr/bin/env python
#implimenting find command
import argparse
import glob
import os
parser = argparse.ArgumentParser(description='this my find commad')
parser.add_argument('start',nargs=1,help='file name or pattern')
parser.add_argument('-name',help='file name or pattern')
parser.add_argument('-print',help='list the file path')
parser.add_argument('-type',help='file type directory(d) or file(f) ')
args=parser.parse_args()
print args.start[0]
print args
filelist=os.listdir(args.start[0])
if args.name:
    for filename in filelist:
        if args.name in  filename:
            if args.type:
                if args.type == 'd':
                    if os.isdir(filename):
                        print filename

            #print filename
