#!/usr/bin/env python3

# last modified by handyc on 12 Nov 2021
# klurp genetic algorithm system for text alignment

# this file is the outermost layer of the klurp system
# which parses user input and invokes the population manager

import sys
import os
import getpass

import glob
from pathlib import Path

import datetime

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

# normalize various witness naming conventions
def normalize(path):
    normalpath=path.replace(".", "_")
    normalpath=normalpath.capitalize()
    return normalpath

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
cleantaisho = os.path.join(klurp, "projects/openphilology/witnesses/cleaned/taisho/")
cleanderge = os.path.join(klurp, "projects/openphilology/witnesses/cleaned/derge/")

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
if argument_count>2:
    path1=sys.argv[1]
    path2=sys.argv[2]

# display usage information
else:
    print("usage:")
    print(shortname + " [witness1] [witness2]")
    print(shortname + " [witness1] [witness2] [popsize]")
    print(shortname + " [witness1] [witness2] [popsize] [generations]")
    print(shortname + " [witness1] [witness2] [popsize] [generations] [mutation rate]")
    print("")
    print("if population size is too low, evolution may not occur properly")
    print("")
    print("examples:")
    print("python3 " + shortname + " T310.31 D75")
    print("python3 " + shortname + " T310.31 D75 100")
    print("python3 " + shortname + " T310.31 D75 100 100")
    print("python3 " + shortname + " T310.31 D75 100 100 7")
    exit()

# if population information passed in, then use it, otherwise use default
if argument_count>3 and sys.argv[3].isnumeric():
    popsize = sys.argv[3]
else:
    popsize = defpopsize

if argument_count>4 and sys.argv[4].isnumeric():
    generations = sys.argv[4]
else:
    generations = defgens

if argument_count>5 and sys.argv[5].isnumeric():
    mutrate = sys.argv[5]
else:
    mutrate = defmut

# Normalize paths to allow confused philologists to name texts in
# various different ways: e.g. T310.31, T310_31, t310.31, t310_31
normal1 = normalize(path1)
normal2 = normalize(path2)

# determine first witness identity (Taisho texts begin with T, otherwise Derge)
# this type of glob matching works well on Linux/Unix systems but fails on Windows,
# so it must be modified to account for slight differences in the ways that
# Windows interprets glob wildcards
if normal1[0]=="T":
    globmatch1 = cleantaisho + "*" + normal1[1:] + "*/*" + normal1[1:] + "*" + ".txt"

else:
    globmatch1 = cleanderge + normal1 + "/" + normal1 + "*" + ".txt"

# locate first requested witness
sortedglob1 = sorted(glob.glob(globmatch1))
if len(sortedglob1) > 0:
    file1 = sortedglob1[0]
    arg1 = file1
else:
    print("Could not find a match for " + globmatch1 + ", quitting")
    exit()

# determine second witness identity (Taisho texts begin with T, otherwise Derge)
# as noted above, Windows chokes on these glob wildcards
if normal2[0]=="T":
    globmatch2 = cleantaisho + "*" + normal2[1:] + "*/*" + normal2[1:] + "*" + ".txt"
else:
    globmatch2 = cleanderge + normal2 + "/" + normal2 + "*" + ".txt"

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
fullcommand = engine + "population.py" + " " + gen + " " + popnum + " " + mut + " " + arg1 + " " + arg2

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
