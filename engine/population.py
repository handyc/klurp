#!/usr/bin/env python3

# this file contains the population manager for the klurp GA system
# this program should not be invoked directly by humans
# but is now only called by klurp.py

# last modification by handyc on 27 Sep 2023

import datetime
import time

import glob
import string

from pathlib import Path

import os
import sys
import random

import multiprocessing

import csv
from agent import agent

#genestring="/home/handyca/data/bls/genes"
genestring="/Users/handyc/data/bls/genes"

#outputstring="/home/handyca/data/bls/output/csv"
outputstring="/Users/handyc/data/bls/output/csv"

# the name of this subprogram
friendlyname = "population manager"

# SLURM

# automatically determine number of threads available
# and use only 3/4 so that computer is not overwhelmed
# or if using SLURM, use requested amount of CPUs from SLURM

try:
    numcores = int(os.environ['SLURM_JOB_CPUS_PER_NODE'])
except:
    numcores = int(multiprocessing.cpu_count()*.75)

if numcores < 1:
    numcores = int(1)

# grab arguments --
# The reason for taking in arguments this way is due to the
# historical development of this system -- initially this file
# was called directly, but now uses a wrapper called klurp.py
# The plan is to replace this section by importing population.py
# and invoking it as a function, but this change requires a number
# of other modifications to other paths and has therefore not
# been implemented yet.

# maximum iterations of GA
maxgen = int(sys.argv[1])

# maximum agents to create
maxagents = int(sys.argv[2])

# mutation rate
mutrate = int(sys.argv[3])

# need at least 2 agents for combination
# so set to 2 if we don't have enough
if maxagents < 2:
    maxagents = 2

# paths to the text files we want to process
text1 = sys.argv[4]
text2 = sys.argv[5]

dictpass = sys.argv[6]



# dictionary
#dictionary = int(sys.argv[6])

# path information for home directory, location of engine and outer layer
home = str(Path.home())
engine = os.path.dirname(__file__)
klurp = os.path.dirname(engine)

# function to generate a gene
def genegen(gene1, gene2, mutrate, genelimit1, genelimit2, genesize):
    newgene = []

    alignmentsize1 = 100
    #alignmentsize2 = 400
    alignmentsize2 = 100

    # genesize should always be greater than zero
    # but just in case it isn't, we set the size to a default value
    # of 1 alignment to prevent divide by zero error
    if genesize < 1:
        genesize = 1

    if alignmentsize1 < 1:
        alignmentsize1 = 1
    if alignmentsize2 < 1:
        alignmentsize2 = 1


    #JUMPY1 = int(genelimit1/genesize)
    #JUMPY2 = int(genelimit2/genesize)
    #JUMPY1 = int(genelimit1/alignmentsize1)
    #JUMPY2 = int(genelimit2/alignmentsize2)
    JUMPY1 = int(alignmentsize1/2)
    JUMPY2 = int(alignmentsize2/2)
    sexual = 1
    # above flag will be set to 0 if we must create a new gene
    
    # if gene1 does not exist, then we must create a gene from scratch
    if not gene1:
        for genecount in range(0, genesize):
            startposition1 = int(genecount * (genelimit1/genesize))
            if startposition1 < 0:
                startposition1 = 0

            endposition1 = startposition1 + alignmentsize1
            if endposition1 > (genelimit1 - 1):
                endposition1 -= JUMPY1

            startposition2 = int(genecount * (genelimit2/genesize))
            if startposition2 < 0:
                startposition2 = 0

            endposition2 = startposition2 + alignmentsize2
            if endposition2 > (genelimit2 - 1):
                endposition2 -= JUMPY2

            # if the beginning of the string comes after the end
            # of the string, then switch the beginning and end
            if startposition1 > endposition1:
                tempswap = startposition1
                startposition1 = endposition1
                endposition1 = tempswap
                #startposition1 = endposition1

            # if the beginning of the string comes after the end
            # of the string, then switch the beginning and end
            if startposition2 > endposition2:
                tempswap = startposition2
                startposition2 = endposition2
                endposition2 = tempswap
                #startposition2 = endposition2

            gene1.append((startposition1, endposition1, startposition2, endposition2))
            # I think we must also create a new gene2 here to avoid problems below
            # added sexual flag to fix this temporarily
            sexual = 0

    for genecount in range(0,genesize):

        # generate a random number to see if mutation should occur
        mutation_roll = random.randint(0, 100)

        # randomly select a parent
        which_parent = random.randint(0,sexual)

        # if mutation occurs, then implement the mutation
        # This section is a bit messy and could be further optimized,
        # but it works as a proof of concept.
        if (mutation_roll < mutrate):
            if (which_parent < 1):
                startposition1 = gene1[genecount][0]
                endposition1 = gene1[genecount][1]
                startposition2 = gene1[genecount][2]
                endposition2 = gene1[genecount][3]
            else:
                startposition1 = gene2[genecount][0]
                endposition1 = gene2[genecount][1]
                startposition2 = gene2[genecount][2]
                endposition2 = gene2[genecount][3]

            distort_component = random.randint(0, 7)
            if distort_component == 0:
                startposition1 += random.randint(0, JUMPY1)
                if startposition1 > (genelimit1 - 1):
                    startposition1 -= random.randint(0, JUMPY1)

            elif distort_component == 1:
                endposition1 += random.randint(0, JUMPY1)
                if endposition1 > (genelimit1 - 1):
                    endposition1 -= random.randint(0, JUMPY1)
                    
            elif distort_component == 2:
                startposition2 += random.randint(0, JUMPY2)
                if startposition2 > (genelimit2 - 1):
                    startposition2 -= random.randint(0, JUMPY2)

            elif distort_component == 3:
                endposition2 += random.randint(0,JUMPY2)
                if endposition2 > (genelimit2 - 1):
                    endposition2 -= random.randint(0, JUMPY2)

            elif distort_component == 4:
                startposition1 -= random.randint(0, JUMPY1)
                if startposition1 < 0:
                    startposition1 += random.randint(0, JUMPY1)

            elif distort_component == 5:
                endposition1 -= random.randint(0, JUMPY1)
                if endposition1 < 0:
                    endposition1 += random.randint(0, JUMPY1)
                    
            elif distort_component == 6:
                startposition2 -= random.randint(0, JUMPY2)
                if startposition2 < 0:
                    startposition2 += random.randint(0, JUMPY2)

            elif distort_component == 7:
                endposition2 -= random.randint(0,JUMPY2)
                if endposition2 < 0:
                    endposition2 += random.randint(0, JUMPY2)

                    
            if startposition1 > endposition1:
                tempswap = startposition1
                startposition1 = endposition1
                endposition1 = tempswap
                #startposition1 = endposition1

            if startposition2 > endposition2:
                tempswap = startposition2
                startposition2 = endposition2
                endposition2 = tempswap
                #startposition2 = endposition2

            newgene.append((startposition1, endposition1, startposition2, endposition2))
        else:
            if which_parent < 1:
                parentseg = gene1[genecount]
            else:
                parentseg = gene2[genecount]
            newgene.append(parentseg)
    return newgene

def population(gen, size, mutrate, text1, text2, dictpass):
    """thread worker function"""

    # inform the user about which texts are being used
    # This is mainly just a check to determine that we have located
    # the correct witnesses.
    print("text1: " + text1)
    print("text2: " + text2)
    #print("dictionary: " + dictloc)

    # create a shortened name from the full pathname of each text
    text1short = os.path.splitext(os.path.basename(text1))[0]
    text2short = os.path.splitext(os.path.basename(text2))[0]

    # this string becomes a directory name for genes working
    # on these two witnesses only
    # Each alignment pair receives its own separate population of genes
    w1_w2 = str(text1short + "_" + text2short)

    # create the appropriate path for this alignment pair's genes
    genedir = os.path.join(klurp, genestring, w1_w2)

    # all csv output files go to the same location for easy access
    csvdir = os.path.join(klurp, outputstring)

    # information concerning the initialization time of this population
    start = datetime.datetime.now()

    timeformat = "%Y%m%dT%H%M%S.%f"
    displayformat = "%Y-%m-%dT%H:%M:%S.%f"

    fstart = start.strftime(timeformat)
    fstartdisplay = start.strftime(displayformat)

    print("started " + friendlyname + " at " + str(fstartdisplay))
    print("comparing performance of " + str(maxagents) + " agents for " + str(maxgen) + " generations" + " on " + str(numcores) + " threads")

    with open(text1) as j1:
        jread1 = j1.read()
        numchars1 = len(jread1)

    with open(text2) as j2:
        jread2 = j2.read()
        numchars2 = len(jread2)

    print("text1 length: " + str(numchars1))
    print("text2 length: " + str(numchars2))

    #####

    # clear out winners
    winner1 = []
    winner2 = []

    # open most recent gene population from genes

    # if this alignment pair does not have a directory for genes,
    # create one now
    if not os.path.exists(genedir):
        os.makedirs(genedir)

    # otherwise retrieve the most recent set of genes by timestamp
    else:
        globmatch = genedir + "/*.txt"
        sortedglob = sorted(glob.glob(globmatch), reverse=True)

        if sortedglob:
            seedfile1 = sortedglob[0] # most recent pop has agents
            print("gene file:" + str(seedfile1))

            # seed a new generation from the retrieved file
            seedgeneration = seedfile1

            places = []
            list1 = []
            list2 = []
            with open(seedgeneration, 'r') as seedf:
                for line in seedf:
                    # remove linebreak which is the last character of the string
                    currentPlace = line[:-1]
                    places.append(currentPlace)

                list1 = places[0].strip().split(" ")
                list2 = places[1].strip().split(" ")

                # alignments have 4 components:
                # begin/end of text 1 fragment, begin/end of text 2 fragment
                for a, b, c, d in zip(*[iter(list1)]*4):
                    winner1.append((int(a), int(b), int(c), int(d)))

                for a, b, c, d in zip(*[iter(list2)]*4):
                    winner2.append((int(a), int(b), int(c), int(d)))
        else:
            pass

    ########################
    mutation = mutrate

    genelimit1 = numchars1
    genelimit2 = numchars2

    genesize1 = int(numchars1 / 10)
    genesize2 = int(numchars2 / 10)

    mingenesize = 100

    if genesize1 < mingenesize:
        genesize1 = mingenesize

    if genesize2 < mingenesize:
        genesize2 = mingenesize

    #genesize1 = int(20)
    #genesize2 = int(20)

    # determine which of two potential gene sizes is smaller
    # and use the smaller one
    if genesize1 < genesize2:
        genesize = genesize1
    else:
        genesize = genesize2

    # notify user of current genesize and mutation settings
    # genesize is the number of individual alignments we want to have
    print("genesize: " + str(genesize))
    print("mutation: " + str(mutation))

    ########################

    for generation in range(0, maxgen):
        gene = []

        # if a winner does not exist, generate a gene from scratch
        if not winner1:
            for x in range(0,maxagents):
                nothing = []
                gene.append(genegen(nothing, nothing, mutation, genelimit1, genelimit2, genesize))

        # otherwise combine 2 parents with mutation
        # this process is essentially the same as sexual reproduction
        else:
            for x in range(0,maxagents):
                gene.append(genegen(winner1, winner2, mutation, genelimit1, genelimit2, genesize))

        # Now we send each gene to an individual agent
        # Initialize each agent as a separate process
        with multiprocessing.Pool(processes=numcores) as pool:
            args = [(text1,text2, gene[x], dictpass,) for x in range(0,maxagents)]
            results = pool.starmap(agent, args)
        # agents have now completed execution at this point

        # determine winning agent by sorting on return scores
        sordid = sorted(range(len(results)), key=results.__getitem__, reverse=True)

        # store the top two winners for the next iteration
        winnerdex1 = sordid[0]
        winner1 = gene[winnerdex1]
        winnerdex2 = sordid[1]
        winner2 = gene[winnerdex2]

        # winner indexes used to determine parent gene for next generation
        winnerscore1 = results[winnerdex1]
        winnerscore2 = results[winnerdex2]

        # retrieve the current time
        now = datetime.datetime.now().strftime(displayformat)
        print(now + ": generation " + str(generation) + " winner is agent " + str(winnerdex1) + " with score " + str(winnerscore1) + ", winner2 is agent " + str(winnerdex2) + " with score " + str(winnerscore2))

    # inform the user that the complete run has ended
    print(friendlyname + " completed " + str(maxgen) + " generations")

    # generate a timestamped filename for the gene output
    nowname = str(fstart) + ".txt"
    print("writing out population file as " + nowname)

    outputgene = os.path.join(genedir, nowname)

    #actually write out the file to /genes
    f = open(outputgene, "w")
    for x in range(0, maxagents):
        for item in gene[sordid[x]]:
            for subitem in item:
                f.write(str(subitem) + " ")
        f.write("\n")
    f.close()


    # create csv output dir if does not exist
    if not os.path.exists(csvdir):
        os.makedirs(csvdir)

    # generate a timestamped filename for the human readable csv output
    csvname = str(fstart) + ".csv"
    outputcsv = os.path.join(csvdir, csvname)

    # actually write out the file to output directory
    with open(outputcsv, 'w', newline='') as newcsv:
        outputwriter = csv.writer(newcsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # save only the winner to prevent giant csv files --
        # these files are used only for human checks of the alignments,
        # as the full data are contained in the genes themselves
        for x in range(0, 1):
            for item in gene[sordid[x]]:
                row = []
                row.append(jread1[item[0]:item[1]])
                row.append(jread2[item[2]:item[3]])
                outputwriter.writerow(row)

    ####################################################################

    # various ways of displaying the time
    finish = datetime.datetime.now()
    ffinish = finish.strftime(timeformat)
    ffinishdisplay = finish.strftime(displayformat)

    totaltime = finish - start

    ####
    print(friendlyname + " ran from " + str(fstartdisplay) + " to " + str(ffinishdisplay))
    print(friendlyname + " execution time: " + str(totaltime))
    return

if __name__ == '__main__':
    population(maxgen, maxagents, mutrate, text1, text2, dictpass)
