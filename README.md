# klurp

## a text engine for anything

***

***

### klurp is a general purpose toolkit for making custom
### language apps for any languages to do any computational tasks
#### (documentation in process)

#
# 1. Introduction
#

Klurp is primarily a text alignment system that employs a simple genetic algorithm to find semantic matches between arbitrary texts. It was initially created in order to align classical Chinese and Tibetan translations of Buddhist texts originally composed in Sanskrit, for the ERC Open Philology project. The system is language agnostic in the sense that it will work on texts in any languages, so long as multi-lingual dictionaries are available for it to utilize.

The main engine is contained in the 'engine' folder in this repository. It is meant to be called by the klurp.py wrapper program, which parses user input. The engine can also be called directly in special instances where the wrapper is not desired.

The samplefiles folder and mkklurp program create a Django project meant to interact with the klurp engine and the data it produces, so that complete interactive web portals can be created from these data very quickly.

Klurp is undergoing major changes right now as we continue to process new materials in Chinese, Tibetan and Sanskrit.
A new release for Klurp is planned for April 2023.

``    February 2023               March 2023                   April 2023         ``  
`` Su Mo Tu We Th Fr Sa        Su Mo Tu We Th Fr Sa         Su Mo Tu We Th Fr Sa  ``      
``           1  2  3  4                  1  2  3  4                            1  ``  
``  5  6  7  8  9 10 11         5  6  7  8  9 10 11          2  3  4  5  6  7  8  ``  
`` 12 13 14 15 16 17 18        12 13 14 15 16 17 18          9 10 11 12 13 14 15  ``  
`` 19 20 21 22 23 24 25        19 20 21 22 23 24 25         16 17 18 19 20 21 22  ``  
`` 26 27 28                    26 27 28 29 30 31            23 24 25 26 27 28 29  ``    
``                                                          30                    ``  
                                                        
![i](https://openphilology.eu/media/pages/news/524279882-1558970201/newsdatech2019.05.png)


<details><summary>History</summary>

Klurp began as the successor to my simple n-grams extraction program, ![aks](https://github.com/handyc/aks).
That program was lacking a user interface as well as other features that
became desirable as I continued to explore patterns in texts.

</details>

<details><summary>Use Cases</summary>

Klurp was initially created with a specific need for locating and
interacting with text patterns in Sanskrit, Tibetan and Chinese
Buddhist texts.

</details>

<details><summary>UTF-8</summary>

Klurp uses UTF-8 by default in order to avoid common problems with non-roman character sets.
Klurp has been tested on Tibetan and Chinese character sets primarily and is in the process of
adding tests for many other character sets.

</details>

<details>
<summary>Text Alignment</summary>

+ Sample alignment from [Gaṅgottaraparipṛcchā](https://www2.hf.uio.no/polyglotta/index.php?page=fulltext&vid=1179&view=fulltext):
    +  ``’di skad bdag gis thos pa dus gcig na | bcom ldan ’das mnyan yod na rgyal bu rgyal byed kyi tshal mgon med zas sbyin gyi kun dga' ra ba na bzhugs te |``  
    + ``如是我聞。一時佛在舍衛國祇樹給孤獨園。``  

+ Sample alignment vinaya
+ Sample alignment sutra
+ Sample alignment abhidharma
  
</details>

<details><summary>DH Course</summary>

course week by week
+ Week 1
    + https://dhtools.org
    + ssh
+ Week 2
    + bash
+ Week 3
    + example 1
    + example 2
+ Week 4
    + example 1
    + example 2
+ Week 5
    + example 1
    + example 2
+ Week 6
    + example 1
    + example 2
+ Week 7
    + example 1
    + example 2
+ Week 8
    + example 1
    + example 2
+ Week 9
    + example 1
    + example 2
+ Week 10
    + example 1
    + example 2
+ Week 11
    + example 1
    + example 2
+ Week 12
    + example 1
    + example 2
+ Week 13
    + example 1
    + example 2


</details>

# Text alignment basics:
    + example text A
    + example text B
    
    alignment process:
      -
      -
      -
      
    


# Recent Events:
### 5 Nov 2021
<details><summary>Full Stack Language Apps from the Bottom Up: Custom Online Portals for Humanities Research Using Linux, Python, Django & other Open Source Tools
</summary>

![LUCDH](https://openphilology.eu/media/pages/partners/1327078252-1625255917/lucdhweb.png)
Join us for the LUCDH lunchtime talk presented by Dr. Christopher Handy  on Wednesday, 3 November at 12:00 – 13:00.

Location: on-campus in the Digital Lab P.J. Veth 1.07 or online via Kaltura Live Rooms. 

Christopher Handy will provide an overview of the major components he uses in his Digital Humanities course at Leiden University, ‘Constructing Digital Language Toolkits’. Now in its fourth iteration, the course helps bridge the gap between traditional humanities language research and web technologies.

Students with no prior background in software design learn to combine general purpose computing resources to create professional quality language toolkits for their specific research needs. Past projects created for the course include online multilingual dictionaries, language tagging engines, educational games, and various other useful applications.

This system places an emphasis on practical methods for bringing existing research projects to the digital realm quickly and easily. The modular design of this stack is especially useful for creating and maintaining dynamic solutions for low resource languages, for which specialized software is often limited or unavailable within the mainstream market.

To Register: Please email: lucdh@hum.leidenuniv.nl 
We very much hope that you can join this live event in the Digital Lab in P.J. Veth 1.07.  However, we will also be live-streaming on Kaltura, so please let us know if you will be attending in person or would like Kaltura Live Room login details.

</details>


### https://www.universiteitleiden.nl/en/events/2021/11/lucdh-lunchtime-speaker-series-christopher-handy
#


