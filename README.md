# klurp

## a text engine for anything

***

***

### klurp is a general purpose toolkit for making custom
### language apps for any languages to do any computational tasks
#### (documentation in process)

***

***

#
# 1. Introduction
#

Klurp is primarily a text alignment system that employs a simple genetic algorithm to find semantic matches between arbitrary texts. It was initially created in order to align classical Chinese and Tibetan translations of Buddhist texts originally composed in Sanskrit, for the ERC [Open Philology](https://cordis.europa.eu/project/id/741884) project. With additional feedback from scholars in other areas of language research, this system was then extended for use with a wide variety of applications across any language pairs. It uses multi-lingual dictionaries to compare similarities of strings, or when these are unavailable it creates
dictionaries from previously seen source materials.

The main engine for Klurp is contained in the 'engine' folder in this repository. It is meant to be called by the klurp.py wrapper program, which parses user input. The engine can also be called directly in special instances where the wrapper is not desired.

The samplefiles folder and mkklurp program create a Django project meant to interact with the klurp engine and the data it produces, so that complete interactive web portals can be created from these data very quickly.

Klurp is undergoing major changes right now as we continue to process new materials in Chinese, Tibetan and Sanskrit.
- Additional languages are being added.
- Additional dictionaries are being added.
- Documentation is being improved.
- new engine tests
- new tutorials
- article on proof of concept

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

+ Sample alignments from [vinaya texts](https://sites.google.com/site/sikkhamana/overview):
    +  <details><summary>``96. yā puna bhikṣuṇī ūna-viṁśati-varṣāṁ kumārī-bhūtāṁ upasthāpayet pācattikaṁ``</summary>lokottaravāda prātimokṣa https://sites.google.com/site/bhikkhunipatimokkha/lokottaravada:8rulesonsikkhamana2yearstr</details>  
    +  <details><summary>``96. 若比丘尼。與減二十雨童女。受具足者波夜提。``</summary>[mahāsāṅghika prātimokṣa](https://sites.google.com/site/bhikkhunipatimokkha/mahasanghika:8rulesonsikkhamana2yearstra)</details>
    +  <details><summary>``104. 若比丘尼。與未滿十二歲已嫁女受具足戒。波逸提。``</summary>[mahīśāsaka prātimokṣa](https://sites.google.com/site/bhikkhunipatimokkha/mahisasaka:8rulesonsikkhamana2yearstrain)</details>  
    +  <details><summary>``108. 若比丘尼。畜未滿十二歲已嫁女為眾。波夜提。``</summary>[sarvāstivāda prātimokṣa](https://sites.google.com/site/bhikkhunipatimokkha/sarvastivada:9rulesonsikkhamana2yearstra)</details>
    +  <details><summary>``108 . 若復苾芻尼知曾嫁女人年未滿十二。與出家者。波逸底迦。``</summary>[mūlasarvāstivāda prātimokṣa](https://sites.google.com/site/bhikkhunipatimokkha/mulasarvas(chinese):6rulesonsikkhamanatr)</details>
   
+ Sample alignment [sutta](https://suttacentral.net/mn12)
+ Sample alignment sutra
+ [rkts tibetan canons](https://github.com/brunogml/rKTs)
+ https://www2.hf.uio.no/polyglotta/index.php?page=fulltext&vid=511&view=fulltext
     +  utpādātyantavighno ’nyo nirodho ’pratisaṃkhyayā || 1.6 || 
     + 偈曰 恒遮欲生生 別有非擇滅 
     + 永礙當生得非擇滅 
     + | skye la gtan du bgegs byed pa | ’gog gźan so sor brtags min pas | 
+ Sample alignment [abhidharma](https://www.academia.edu/35577177/A_translation_of_the_quotations_in_%C5%9Aamathadevas_Abhidharmako%C5%9Bop%C4%81yik%C4%81_%E1%B9%AD%C4%ABk%C4%81_parallel_to_the_Chinese_Sa%E1%B9%83yukta_%C4%81gama_discourses_231_238_240_245_252_and_255)
+ https://read.84000.co/translation/toh72.html  
</details>


<details><summary>color test</summary>
$\fcolorbox{yellow}{lime} {96. yā puna bhikṣuṇī } \colorbox{white}{red} {ūna-viṁśati-varṣāṁ kumārī-bhūtāṁ upasthāpayet pācattikaṁ}$  
$\color{lime}{96. yā puna bhikṣuṇī }  \ \ \color{red}{ūna-viṁśati-varṣāṁ kumārī-bhūtāṁ upasthāpayet pācattikaṁ}$  
  
$\fcolorbox{yellow}{lime} {"96. 若比丘尼。"} \colorbox{white}{red} {與減二十雨童女。受具足者波夜提。}$  

$\fcolorbox{yellow}{lime} {104. 若比丘尼。} \colorbox{white}{red} {與未滿十二歲已嫁女受具足戒。波逸提。}$  

$\fcolorbox{yellow}{lime} {108. 若比丘尼。} \colorbox{white}{red} {畜未滿十二歲已嫁女為眾。波夜提。}$  

$\fcolorbox{yellow}{lime} {108 . 若復苾芻尼知} \colorbox{white}{red} {曾嫁女人年未滿十二。與出家者。波逸底迦。}$  

$\mathscr{\color{red}{yā puna bhikṣuṇī} \ \ \color{blue}{ūna-viṁśati-varṣāṁ } \ \ \color{yellow}{kumārī-bhūtāṁ upasthāpayet pācattikaṁ}}$
$\color{red}{yā puna bhikṣuṇī} \ \ \color{blue}{ūna-viṁśati-varṣāṁ } \ \ \color{yellow}{kumārī-bhūtāṁ upasthāpayet pācattikaṁ}$  
  
$\mathscr{\color{red}{this} \ \ \color{blue}{is \ \ a \ \ paragraph} \ \ \color{yellow}{in \ \ another \ \ font}}$

</details>

<details><summary>n-grams test</summary>
$\color{lime}{96. yā puna bhikṣuṇī }$  
  
$\color{lime} {96. 若比丘尼。}$  

$\color{lime} {104. 若比丘尼。}$  

$\color{lime} {108. 若比丘尼。}$  

$\color{lime} {108 . 若復苾芻尼知}$  

</details>
  
<details><summary>web interface</summary>

Klurp uses the Django web framework to create simple app interfaces easily.
Klurp includes various scripts to automate the creation of these apps.

Link to Klurp demo page [coming soon](https://github.com)

</details>

<details><summary>DH Course</summary>

I have received numerous requests for the course materials associated with
the digital humanities course I created and taught at Leiden University
from 2018 through 2021. I have started putting these materials online and
will soon move them to a [separate repository](https://github.com/handyc/dhtools.org/tree/main/courses/dhtoolkits) for easier access.

</details>

# Text alignment basics:
    + example text A
    + example text B
    
    alignment process:
      -
      -
      -
      
# additional features
    + automatic n-grams statistics
    + automatic dictionary creation
    + automatic alignment from current information
    + continuously updated alignments
    + user input through simple web interface
    + basic custom django app for unique data from template
    + engine automatically adjusts to available processors
    + step based system preserves data across generations automatically, easy to archive
    + easy to extend with custom code
      
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


