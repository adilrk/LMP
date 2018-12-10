#!/usr/bin/env python
import argparse
parser=argparse.ArgumentParser('testing cmd line')
parser.add_argument('--foo','-f',help='some argument')
parser.add_argument('--foo1','-f1',help='some argument foo1')
parser.add_argument('--foo2','-f2',help='some argumentfoo2')
args=parser.parse_args()
print args
