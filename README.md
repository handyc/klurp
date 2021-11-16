# klurp

## a text engine for anything

***

`git clone https://github.com/handyc/klurp.git`

`ln -s ~/klurp/mkklurp.py ~/scripts/mkklurp`

`chmod 700 ~/klurp/mkklurp.py`

`pip3 install sh`

`mkklurp [environment] [project] [app]`

`mkklurp [environment] [project]`

`mkklurp [environment]`

***

### documentation in progress

#
# 1. Introduction
#

Klurp is primarily a text alignment system that employs a simple genetic algorithm to find
semantic matches between arbitrary texts. It was initially created in order to align
classical Chinese and Tibetan translations of Buddhist texts originally composed in Sanskrit,
for the ERC Open Philology project. The system is language agnostic in the sense that it will
work on texts in any languages, so long as multi-lingual dictionaries are available for it to
utilize.

The main engine is contained in the 'engine' folder in this repository.
It is meant to be called by the klurp.py wrapper program, which parses user input.
The engine can also be called directly in special instances where the wrapper is not desired.

The samplefiles folder and mkklurp program create a Django project meant to interact with
the klurp engine and the data it produces, so that complete interactive web portals can be
created from these data very quickly.

Klurp is still in a beta testing phase. More documentation will be added here over the
coming months.

![i](https://openphilology.eu/media/pages/news/524279882-1558970201/newsdatech2019.05.png)



 79 days until Klurp v. 1.0 New Year's release party

````
                            2021
      October               November              December        
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  
                1  2      1  2  3  4  5  6            1  2  3  4  
 3  4  5  6  7  8  9   7  8  9 10 11 12 13   5  6  7  8  9 10 11  
10 11 12 13 14 15 16  14 15 16 17 18 19 20  12 13 14 15 16 17 18  
17 18 19 20 21 22 23  21 22 23 24 25 26 27  19 20 21 22 23 24 25  
24 25 26 27 28 29 30  28 29 30              26 27 28 29 30 31     
31                                                                
