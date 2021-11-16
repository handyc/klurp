from pathlib import Path

import os
import sys
import csv

# retrieve path locations for various elements of the system
home = str(Path.home())
engine = os.path.dirname(__file__)
klurp = os.path.dirname(engine)

# ideally we receive 3 arguments from population manager
if len(sys.argv) > 3:
    num = int(sys.argv[1])
    text1 = str(sys.argv[2])
    text2 = str(sys.argv[3])

# otherwise, set some defaults where appropriate
elif len(sys.argv) > 2:
    num = 0
    text1 = str(sys.argv[1])
    text2 = str(sys.argv[2])

elif len(sys.argv) > 1:
    num = int(sys.argv[1])
    text1 = "T11n0310_31"
    text2 = "D75"
else:
    num = 0
    text1 = "T11n0310_31"
    text2 = "D75"

def agent(text1, text2, gene):
    """thread worker function"""

    score = 0
    scoredict = 0

    #open the two texts and read their entire content
    j1 = open(text1)
    jread1 = j1.read()
    j1.close()

    j2 = open(text2)
    jread2 = j2.read()
    j2.close()

    # retrieve the location of multilingual dictionaries
    dictloc = os.path.join(klurp, "projects/openphilology/dictionaries")

    # loop through the dictionary directory
    for filename in os.listdir(dictloc):
        if filename.endswith(".txt"):
            thepath = os.path.join(dictloc, filename)

            # open each dictionary and retrieve its contents
            with open(thepath, mode='r') as thefile:
                reader = csv.reader(thefile)
                dictionary = {(rows[0],rows[1]) for rows in reader}

            # retrieve each alignment guess for current agent
            for fragment in gene:
                text1frag = jread1[fragment[0]:fragment[1]]
                text2frag = jread2[fragment[2]:fragment[3]]

                # compare alignment guess to each dictionary term
                for term in dictionary:
                    # ignore blank terms
                    if not term[0] or not term[1]:
                        pass
                    # apply scores for matching terms
                    elif term[0] in text1frag and term[1] in text2frag:
                        scoredict += 11
                    elif term[1] in text1frag and term[0] in text2frag:
                        scoredict += 11

                scoredict-=(len(text1frag)+len(text2frag))

                # penalize blank alignments
                if not text1frag:
                        scoredict -= 1000
                # award points for proper punctuation
                elif text1frag[-1] == '/' or '。':
                        scoredict += 1
                # penalize blank alignments
                if not text2frag:
                        scoredict -= 1000
                # award points for proper punctuation
                elif text2frag[-1] == '/' or '。':
                        scoredict += 1

    # send score back to population manager
    return scoredict
