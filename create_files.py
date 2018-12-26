#!/usr/bin/env python
#this script to create direcotry structor /var/tmp/vault/ then some number and each number will have 4 direcotry flash flashstream livestream and mystream, each these folder will have a.txt b.txt.
import os
import argparse
import random
parser = argparse.ArgumentParser("this to create file stucture")
parser.add_argument("-d",'--dir',help="input direcotory name",default='vault')
args = parser.parse_args()
vartmp = '/var/tmp/'
vaultdir = vartmp + '/' + args.dir
if not os.path.exists(vaultdir):
    try:    
        os.makedirs(vartmp + args.dir )
    except Exception as err:
        print "cannot create direcotory{}".format(err)
    else:
        print "direcoty" + args.dir + " has been created"
    print " creating file"
else :
    print " vault directory exist"
#os.chdir(vartmp + args.dir)
if not os.path.exists(vaultdir+'/'+ '1'):
    print " number direcoty not exist creating it..."
    for num in range(1,10):
        os.makedirs(vartmp + args.dir+'/' + str(num))
else:
    print " number direcoty exist moving forward..."

print " do you like to see directoy structure please enter yes "
lsdir = raw_input(">")
if lsdir == 'yes':
    for directory, subdir, files in os.walk(vaultdir):
        print directory, subdir, files

print " looks like you dont wanted to list the directory , moving forward ... " 

print " creating files flash flashstream livestream in random vault subdirecoty"

for num in range(1,5):
    random_subdir = str(random.randint(1, 10))
    flashdir = vaultdir + '/' + random_subdir + '/' + 'flash'
    #print flashdir
    if os.path.exists(flashdir):
        open(flashdir + '/' + "flash.txt","w").close()
    if not os.path.exists(flashdir):
        os.makedirs(flashdir)
    else:
        print "{} direcoty exist".format(flashdir)

for num in range(1,5):
    random_subdir = str(random.randint(1, 10))
    flashdir = vaultdir + '/' + random_subdir + '/' + 'flashstream'
    if os.path.exists(flashdir):
        open(flashdir + '/' + "flashstream.txt","w").close()
    if not os.path.exists(flashdir):
        os.makedirs(flashdir)
    else:
        print "{} direcoty exist".format(flashdir)

for num in range(1,5):
    random_subdir = str(random.randint(1, 10))
    flashdir = vaultdir + '/' + random_subdir + '/' + 'livestream'
    #print flashdir
    if os.path.exists(flashdir):
        open(flashdir + '/' + "livestream.txt","w").close()
    if not os.path.exists(flashdir):
        os.makedirs(flashdir)
    else:
        print "{} direcoty exist".format(flashdir)

for num in range(1,5):
    random_subdir = str(random.randint(1, 10))
    flashdir = vaultdir + '/' + random_subdir + '/' + 'donotdelete'
    if os.path.exists(flashdir):
        open(flashdir + '/' + "donotdelete.txt","w").close()
    if not os.path.exists(flashdir):
        os.makedirs(flashdir)
    else:
        print "{} direcoty exist".format(flashdir)

print " do you like to see directoy structure please enter yes "
lsdir = raw_input(">")
if lsdir == 'yes':
    for directory, subdir, files in os.walk(vaultdir):
        print directory, subdir, files


