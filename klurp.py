#!/usr/bin/env python3

# last modified by handyc on 27 Sep 2023
# klurp genetic algorithm system for text alignment

# this file is the outermost layer of the klurp system
# which parses user input and invokes the population manager

import sys
import os
import getpass

import glob
from pathlib import Path

import datetime

#taishostring = "/home/handyca/data/bls/"
#dergestring = "/home/handyca/data/bls/"

#text1loc = "/home/handyca/data/bls/"
#text2loc = "/home/handyca/data/bls/"

text1loc = "/Users/handyc/data/bls/"
text2loc = "/Users/handyc/data/bls/"

#text1loc = "data/bls/"
#text2loc = "data/bls/"

#/Users/handyc/data/bls

# the name of this program
friendlyname = "klurp"

# default variables for genetic algorithm
# these will eventually be moved to a human readable settings file
defpopsize = 10
defgens = 1
defmut = 7

# obtain the current time
def now():
    now=datetime.datetime.now()
    return now

# obtain username and current time
user=getpass.getuser()
timeformat="%d %b %Y %H:%M:%S"
start_time = now()
start_string=start_time.strftime(timeformat)

# obtain home directory path
home = str(Path.home())

# obtain klurp directory
klurp = os.path.dirname(__file__)

# obtain the basename of this program
shortname = os.path.basename(sys.argv[0])

# create proper path for engine (population and agent subprograms)
engine = os.path.join(klurp, "engine/")

# create proper paths for cleaned witness files
# for our proof of concept we use texts from only two sources,
# the Taisho canon for Chinese and the Derge Kanjur for Tibetan


#cleantaisho = os.path.join(klurp, "projects/openphilology/witnesses/cleaned/taisho/")
#cleanderge = os.path.join(klurp, "projects/openphilology/witnesses/cleaned/derge/")

#cleantaisho = os.path.join(klurp, taishostring)
#fulltext1 = os.path.join(klurp, text1loc)
fulltext1 = os.path.join("/", text1loc)

#cleanderge = os.path.join(klurp, dergestring)
#fulltext2 = os.path.join(klurp, text2loc)
fulltext2 = os.path.join("/", text2loc)

# determine number of arguments passed in
argument_count=len(sys.argv)

# a friendly greeting with information about start time
print("Welcome to " + friendlyname + ", " + user + "!")
print(friendlyname + " start: " + str(start_string))

# collapse arguments to single string
# There is a reason for using this method instead of a more
# Pythonic function call or via argparse --
# it has to do with providing various different methods for
# calling the system directly or via a Django web interface,
# but this portion will eventually be changed to be more Pythonic

arguments = str(sys.argv[1:argument_count+1])
collapsed = " ".join(sys.argv[1:])
print(str(argument_count-1) + " arguments:", collapsed, " --->")

# check for proper number of arguments (require 2 witnesses, otherwise exit)
if argument_count>6 and sys.argv[4].isnumeric():
#if argument_count>5 and sys.argv[4].isnumeric():
    path1=sys.argv[1]
    path2=sys.argv[2]
    popsize = sys.argv[3]
    generations = sys.argv[4]
    mutrate = sys.argv[5]
    dictloc = sys.argv[6]

# display usage information
else:
    print("usage:")
    print(shortname + " [witness1] [witness2] [popsize] [generations] [mutation rate] [dictionary location]")
    print("")
    print("if population size is too low, evolution may not occur properly")
    print("")
    print("example:")
    print("python3 " + shortname + " T310.31 D75 100 100 7 /Users/handyc/data/bls/example1/dictionaries")
    exit()

# Normalize paths (obsolete)

normal1 = path1
normal2 = path2

globmatch1 = fulltext1 + normal1 + "/*" + ".txt"

# locate first requested witness
sortedglob1 = sorted(glob.glob(globmatch1))
if len(sortedglob1) > 0:
    file1 = sortedglob1[0]
    arg1 = file1
else:
    print("Could not find a match for " + globmatch1 + ", quitting")
    exit()

globmatch2 = fulltext2 + normal2 + "/*" + ".txt"

# locate second requested witness
sortedglob2 = sorted(glob.glob(globmatch2))
if len(sortedglob2) > 0:
    file2 = sortedglob2[0]
    arg2 = file2
else:
    print("Could not find a match for " + globmatch2 + ", quitting")
    exit()

# prepare to invoke population manager
popnum = str(popsize)
gen = str(generations)
mut = str(mutrate)
fullcommand = engine + "population.py" + " " + gen + " " + popnum + " " + mut + " " + arg1 + " " + arg2 + " " + dictloc

# remove extraneous whitespace
fullcommand = fullcommand.strip()

# inform user of fuzzy match for witness input
#print(collapsed + " --->")
print(arg1)
print(arg2)
print("")

# invoke the population manager --
# there is a reason I used this hacky style to invoke the population manager,
# initially the population manager was being called directly,
# but it proved to be difficult for our team to understand --
# eventually this system will be replaced using argparse and
# function calls instead of this ninja method
os.system(fullcommand)

# determine end time
end_time = now()
end_string = end_time.strftime(timeformat)

# determine total execution time
total_time = end_time - start_time

# inform user of start, end and total execution time
print("")
print(friendlyname + " start: " + str(start_string) + " end: " + str(end_string))
print(friendlyname + " total processing time: " + str(total_time))

# This is the end of the program and nothing follows this line
