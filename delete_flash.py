#!/usr/bin/env python 
#find and delete only flash flashsteream livestream in /var/tmp/vault
import os
import sys
import shutil
if not sys.argv[1] :
    print "please provide proper argument"
    print " ./delete_flash --list to list the contenet and ./delete_flash --delete the contgent"
args = sys.argv[1]


if not len(sys.argv) == 2 : 
    print "please provide proper argument"
    print " ./delete_flash --list to list the contenet and ./delete_flash --delete the contgent"

if args == '--list' or args == '-l':
    for directory,subdir,files in os.walk("/var/tmp/vault"):
        print directory,subdir,files
    sys.exit()

if args == '--delete' or args == '-d':
    print " are you sure want to delete flash flashsteream livestream in /var/tmp/vault please \"YES\" to continue "
    answer = raw_input(">")
    if answer == "YES":
        print "deleting flash flashsteream livestream ..." 
        for directory,subdir,files in os.walk("/var/tmp/vault"):
            if "flash" in directory.split('/') or "flashstream" in directory.split('/') or "livestream" in directory.split('/'):
                print "deleting {} ...".format(directory)
                shutil.rmtree(directory)
    else:
        print " Exiting now"
        sys.exit()

else:
    print "Please enter proper info"
    print " ./delete_flash --list to list the contenet and ./delete_flash --delete the contgent"

