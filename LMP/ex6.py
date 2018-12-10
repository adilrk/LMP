#!/usr/bin/env python
#implimenting find command
import argparse
import glob
import os
import sys
parser = argparse.ArgumentParser(description='this my find commad')
parser.add_argument('start',nargs=1,help='file name or pattern')
parser.add_argument('-name',help='file name or pattern')
parser.add_argument('-print',help='list the file path')
parser.add_argument('-type',help='file type directory(d) or file(f) ')
args=parser.parse_args()
filelist=os.listdir(args.start[0])
if args.name:
    for filename in filelist:
        if args.name in  filename:
            if args.type:
                if args.type == 'd':
                    full_path = os.path.join(args.start[0],filename)
                    #print full_path
                    if os.path.isdir(full_path):
                        print filename
                elif args.type == 'f':
                    full_path = os.path.join(args.start[0],filename)
                    if os.path.isfile(full_path):
                        print filename
                else:
                    print "type not supported"
                    sys.exit()
            else:
                print filename
