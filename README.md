# klurp

## a text engine for anything

---
---

### klurp is a general purpose toolkit for making custom

### language apps for any languages to do any computational tasks

---

#### TL;DR -- use the following command to get started (more complex installation method in section 2):

```
git clone https://github.com/handyc/klurp
```

> **Note**
> Be sure to use some version of Python 3 and not Python 2!

---

---

#

# 1. Introduction

#

Klurp is primarily a text alignment system that employs a simple genetic algorithm to find semantic matches between arbitrary texts. It was initially created in order to align classical Chinese and Tibetan translations of Buddhist texts originally composed in Sanskrit, for the ERC [Open Philology](https://cordis.europa.eu/project/id/741884) project. With additional feedback from scholars in other areas of language research, this system was then extended for use with a wide variety of applications across any language pairs. It uses multi-lingual dictionaries to compare similarities of strings, or when these are unavailable it creates
dictionaries from previously seen source materials.

#

# 2. Installation

#

Create a virtual environment using venv
(name it anything you like, i.e. "klurpenv" can be anything you think is sensible):

```
python3 -m venv klurpenv
```

Change your location to the new environment:

```
cd klurpenv
```

Activate the virtual environment:

```
source bin/activate
```

Grab the main klurp files from the klurp github repo:

```
git clone https://github.com/handyc/klurp
```

Use pip to install various external modules:

```
pip install [module-name]
```

Use pip to install Django (if you don't want the Django interface, you don't need to do this part):

```
pip install django-admin
```

Use pip to install Gunicorn (used for a socket server for Django app):

```
pip install gunicorn
```

#

# 3. Setup

#

Change the following directory locations to your preferences:

in klurp.py:

```
text1loc = "/Users/handyc/data/bls/"
text2loc = "/Users/handyc/data/bls/"
```

Above are the locations of the main directories where projects are kept.
Having these variables allows for klurp to be invoked with shorter subdirectory names,
but it's a bit of a hassle changing it for each system. This setting is eventually
going in a separate settings file.

in population.py:

```
genestring="/Users/handyc/data/bls/genes"
outputstring="/Users/handyc/data/bls/output/csv"
```

Above are the locations of the directories where your genes and output files are kept.
These settings will also go in one main settings file eventually. If the named directories
do not exist, they will be created when klurp needs to use them.

#

# 4. Usage

#

Navigate to the virtual environment you created for klurp (here, the virtual environment is named 'klurpenv'):

```
cd klurpenv
```

Be sure to activate the virtual environment before each use:

```
source bin/activate
```

Navigate to the klurp directory inside the virtual environment:

```
cd klurp
```

Run the main klurp.py script as you would any Python script:

```
python klurp.py
```

Supply additional arguments to specify your files, population size, mutation rate and dictionary location:

```
python klurp.py [witness1] [witness2] [popsize] [generations] [mutation rate] [dictionaries directory]
```

example:

```
python3 klurp.py example2/text1 example2/text2 10000 100 3 /Users/handyc/data/bls/example2/dictionaries
```

where "example2" is a subdirectory under "/Users/handyc/data/bls/" (specified in the directory variables above)

The dictionaries directory is specified as a full path in order to make it easy to swap out dictionaries.

This system made sense to me at the time, but I think it is probably very confusing for everyone else,
so my plan is to revamp this section and put all of these things into a settings file soon.

I'm planning to add better argument parsing to klurp very soon, because these arguments are getting way
out of control now! Sorry. The old system had defaults for all of these things, but the system currently
requires you to specify all of these things, otherwise it has no idea what you are trying to do.

When you are done using klurp, you can deactivate the virtual environment with the 'deactivate' command:

```
deactivate
```

#

# 5. Additional Information

#

The main engine for Klurp is contained in the 'engine' folder in this repository. It is meant to be called by the klurp.py wrapper program, which parses user input. The engine can also be called directly in special instances where the wrapper is not desired. The entire system is made to be highly customizable, which is the reason everything is in separate files. If you screw something up,
just remove the virtual environment and try again!

The samplefiles folder and mkklurp program create a Django project meant to interact with the klurp engine and the data it produces, so that complete interactive web portals can be created from these data very quickly.

Klurp is undergoing major changes right now as we continue to process new materials in Chinese, Tibetan and Sanskrit.

- Additional [languages](https://en.wikipedia.org/wiki/ISO_639-3) are being added.
- Additional dictionaries are being added.
- Documentation is being improved.
- new engine tests
- new tutorials
- article on proof of concept coming soon....

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

- Sample alignment from [Gaṅgottaraparipṛcchā](https://www2.hf.uio.no/polyglotta/index.php?page=fulltext&vid=1179&view=fulltext):

  - `’di skad bdag gis thos pa dus gcig na | bcom ldan ’das mnyan yod na rgyal bu rgyal byed kyi tshal mgon med zas sbyin gyi kun dga' ra ba na bzhugs te |`
  - `如是我聞。一時佛在舍衛國祇樹給孤獨園。`

- Sample alignments from [vinaya texts](https://sites.google.com/site/sikkhamana/overview):
  - <details><summary>``96. yā puna bhikṣuṇī ūna-viṁśati-varṣāṁ kumārī-bhūtāṁ upasthāpayet pācattikaṁ``</summary>lokottaravāda prātimokṣa https://sites.google.com/site/bhikkhunipatimokkha/lokottaravada:8rulesonsikkhamana2yearstr</details>
  - <details><summary>``96. 若比丘尼。與減二十雨童女。受具足者波夜提。``</summary>[mahāsāṅghika prātimokṣa](https://sites.google.com/site/bhikkhunipatimokkha/mahasanghika:8rulesonsikkhamana2yearstra)</details>
  - <details><summary>``104. 若比丘尼。與未滿十二歲已嫁女受具足戒。波逸提。``</summary>[mahīśāsaka prātimokṣa](https://sites.google.com/site/bhikkhunipatimokkha/mahisasaka:8rulesonsikkhamana2yearstrain)</details>
  - <details><summary>``108. 若比丘尼。畜未滿十二歲已嫁女為眾。波夜提。``</summary>[sarvāstivāda prātimokṣa](https://sites.google.com/site/bhikkhunipatimokkha/sarvastivada:9rulesonsikkhamana2yearstra)</details>
  - <details><summary>``108 . 若復苾芻尼知曾嫁女人年未滿十二。與出家者。波逸底迦。``</summary>[mūlasarvāstivāda prātimokṣa](https://sites.google.com/site/bhikkhunipatimokkha/mulasarvas(chinese):6rulesonsikkhamanatr)</details>
- https://www2.hf.uio.no/polyglotta/index.php?page=fulltext&vid=511&view=fulltext + utpādātyantavighno ’nyo nirodho ’pratisaṃkhyayā || 1.6 || + 偈曰 恒遮欲生生 別有非擇滅 + 永礙當生得非擇滅 + | skye la gtan du bgegs byed pa | ’gog gźan so sor brtags min pas |
</details>

<details><summary>web interface</summary>

Klurp uses the Django web framework to create simple app interfaces easily.
Klurp includes various scripts to automate the creation of these apps.

Link to Klurp demo page [coming soon](https://philology.dhtools.org)

</details>

<details><summary>DH Course</summary>

I have received numerous requests for the course materials associated with
the digital humanities course I created and taught at Leiden University
from 2018 through 2021. I have started putting these materials online and
will soon move them to a [separate repository](https://github.com/handyc/dhtools.org/tree/main/courses/dhtoolkits) for easier access.

</details>

#

# 6. Text alignment basics

#

Article coming soon.

#

# 7. Creating Custom Dictionaries

#

Dictionaries are standard CSV files that follow a simple format:

term1,term2

You can create dictionaries for any language pairs using any unicode characters.
Use UTF-8 format only to prevent unpredictable results!

Example dictionary entry:

"恒河上","gang gā'i mchog"

You can have multiple dictionaries for a single pair of texts.
The klurp system expects texts and dictionaries in the following directory format:

```
projectname/
├── dictionaries/
│   ├── dict1.csv
│   ├── dict2.csv
│   └── anyname.csv
├── text1/
│   └── anyname.txt
└── text2/
    └── anyname.txt

```

\*Actually, I changed my mind, you can put the dictionaries anywhere you like now,
but it makes sense to put them in the same place as your other texts so that you can
keep track of them.

#

# 8. Additional Features

#

<details><summary>automatic n-grams statistics (see my n-grams utility, aks)</summary>
https://github.com/handyc/aks
This feature is being merged into the main klurp repo but is not yet available here --
for the time being please use the aks repo to generate n-grams for your texts.
</details>

<details><summary>automatic dictionary creation (this feature is not completely working yet)</summary>
This feature is being merged into the main klurp repo but is not yet available here --
for the time being please use the aks repo to generate n-grams for your texts.
</details>

<details><summary>continuously updated alignments</summary>
(using Django management commands and cron) -- documentation on this feature in progress
</details>

<details><summary>user input through simple web interface</summary>
Django interface -- documentation in progress
</details>

<details><summary>basic custom django app for unique data from template</summary>
see samplefiles to get started making your own custom Django interface for your project's specific needs
</details>

<details><summary>engine automatically adjusts to available processors</summary>
The klurp system detects the number of processors available and sets itself to use a custom-defined
percentage of that total, in order to prevent itself from completely taking over your machine.
Klurp has also been tested successfully on SLURM systems and can autodetect if SLURM is available
and the number of available processors. The code is fairly simple and well commented, so you should
be able to modify it to work on other cluster setups as well. Please contact me if you are interested
in working together to add these types of features.
</details>

<details><summary>basic custom django app for unique data from template</summary>
see samplefiles to get started making your own custom Django interface for your project's specific needs
</details>

<details><summary>easy to extend with custom code</summary>
Klurp was designed from scratch with a mind toward messy data files acquired from various sources.
It is made to be easy to customize for any languages, any file formats, etc.
</details>

<details><summary>step based system preserves data across generations automatically, easy to archive</summary>
Klurp remembers its last state based on datetime-stamped gene files, so that you can always pick up
where you left off. The gene files are very portable, meaning that you can transfer them to another system
without losing any information.
</details>

#

# 9. Sample Files

#

The files in the samplefiles directory are mostly unfinished, and meant to be used as templates for
getting started with a custom Django app linked to the main klurp engine. You don't need any of the
files in samplefiles in order to run the klurp engine, but they may be helpful in getting some ideas
of the different types of projects that are possible to create.

#

# 10. Frequently Asked Questions

#

Q: Have you considered using an LLM (large language model) instead of this system?

A: Yes. LLMs have done various amazing things recently. The initial project for which klurp was created
did not have anything close to the amount of training data that would be needed for using such a solution
successfully. It is certainly possible that there are other text alignment projects for which an LLM would
be more effective than klurp, especially in cases where large amounts of training data are available. The
main benefit of using klurp is that it does not require any training data at all, which makes it ideal for
low resource languages and projects where the source files are very messy.

Q: Is this an automated text translator?

A: Klurp was created for use as a text alignment engine, which is not directly related to the task of
machine translation. If you are looking for a program that translates from one language to another, klurp
is probably not what you are looking for.

Q: What happened to all of the dictionaries? Why don't you supply dictionaries for X/Y/Z language?

A: Some sample dictionaries for klurp are available in the samplefiles folder. I am unfortunately not able
to distribute various traditional multilingual dictionaries due to intellectual property restrictions.
You can always convert dictionaries that you acquire from other sources into the simple .CSV format used
by the klurp system (how you go about doing this conversion depends largely on the format of the source files).

See for example:

[here](https://www2.hf.uio.no/polyglotta/index.php?page=volume&vid=263)

and

[here](https://buddhistinformatics.dila.edu.tw/glossaries/glossaries.php)

#

# 11. Recent / Upcoming Events

#

### 29 September 2023

<details><summary>Automated Alignment of Vinaya Texts: an Evolutionary Strategy
</summary>

[Buddhism and Law: Third International Conference](https://www.buffalo.edu/baldycenter/events/conferences/buddhism-2023.html)

Abstract: This presentation demonstrates a novel method for automated crosslinguistic alignment of vinaya (monastic law) texts in Sanskrit, Tibetan, Chinese and other languages using a simple but effective genetic algorithm, with an example implementation in Python, and a Django web interface. Text alignment is a process of locating similar passages across different versions of documents. The degree to which two passages are similar is a matter open to debate; what similarity means in literature may be mathematically undefinable, due to the non-logical structure of human language. Vinaya texts occur in multiple versions for various reasons, including translations, document drafts, sectarian disagreements, and other phenomena of text transmission. They serve as a good case study for text alignment problems in general. While some alignments between texts may seem obvious to human readers, there are also instances where alignment boundaries are ambiguous or unresolvable even for trained specialists. It is therefore nontrivial to perform the same task on a computer and achieve quality results without intervention from the user. The system described here is open source and free for anyone to use and modify, without restrictions. It can be run on personal computers, cluster computers, mobile phones, and various other computing devices.

</details>

### 6 June 2023

<details><summary>Cross-linguistic Text Alignment: An Evolutionary Approach
</summary>

[ALICE-SHARK User Meeting 2023](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37520053/ALICE-SHARK+User+Meeting+2023)

Abstract: Text alignment is the process of finding similar passages across two or more documents. Text alignment is a process that can be useful in examining multiple versions of a document, whether in one or several languages, or in searching for text re-use within a collection of disparate documents. Some examples of the types of projects that benefit from text alignment include: 1) matching parallel readings of Bible passages across different translations, 2) compiling multiple versions of "Little Red Riding Hood" or other popular narratives, and 3) locating thematically similar texts within a larger corpus (e.g. finding medical literature within a Buddhist canon). Traditionally, the process of text alignment is done by a human being, and the determination of the boundaries of aligned segments is largely intuited from the education and experience of the researcher.

However, if we attempt to automate this process, we quickly find that defining formally what similarity means can be a non-trivial task. This talk focuses on one particular solution to this problem, developed initially for a project in Buddhist Studies but then generalised to cover a wide variety of text alignment problems across any languages and genres. The basic idea is that the data presented to us are always in a less than ideal state, and that alignment of any two passages can never have a single correct solution. Instead of attempting to achieve perfect alignments, my method is to approach a hypothetical ideal alignment through an iterative process that begins with a series of educated guesses about aligned passages and then refines those guesses using a customisable scoring system. I use a simple genetic algorithm, designed in Python, to create a population of "agents" that each possess a sequence of data called a "gene" that dictates the alignment guesses each agent makes about a set of texts. Agents assign scores to themselves based on dictionary matches and other information, and a master controller combines the genes of the top scoring agents to create the next generation of agents. Over multiple generations, these agents evolve toward desired alignments, in a way that is similar to dog breeding or other processes of artificial selection among biological organisms. The system I have designed is free, open source and easy to use, allowing a researcher to select population sizes, mutation rates, scoring mechanisms and other variables to suit any particular alignment project. This software is also made to run on nearly any device, including cluster computers (e.g. the Leiden ALICE cluster), personal computers, mobile phones, and even Raspberry Pi and other single board computers.

</details>

### 21 April 2023

<details><summary>Cross-linguistic Text Alignment: An Evolutionary Approach
</summary>

[Leiden HumAN](https://lu-human.github.io)

Abstract: Text alignment is the process of finding similar passages across two or more documents. Text alignment is a process that can be useful in examining multiple versions of a document, whether in one or several languages, or in searching for text re-use within a collection of disparate documents. Some examples of the types of projects that benefit from text alignment include: 1) matching parallel readings of Bible passages across different translations, 2) compiling multiple versions of "Little Red Riding Hood" or other popular narratives, and 3) locating thematically similar texts within a larger corpus (e.g. finding medical literature within a Buddhist canon). Traditionally, the process of text alignment is done by a human being, and the determination of the boundaries of aligned segments is largely intuited from the education and experience of the researcher.

However, if we attempt to automate this process, we quickly find that defining formally what similarity means can be a non-trivial task. This talk focuses on one particular solution to this problem, developed initially for a project in Buddhist Studies but then generalised to cover a wide variety of text alignment problems across any languages and genres. The basic idea is that the data presented to us are always in a less than ideal state, and that alignment of any two passages can never have a single correct solution. Instead of attempting to achieve perfect alignments, my method is to approach a hypothetical ideal alignment through an iterative process that begins with a series of educated guesses about aligned passages and then refines those guesses using a customisable scoring system. I use a simple genetic algorithm, designed in Python, to create a population of "agents" that each possess a sequence of data called a "gene" that dictates the alignment guesses each agent makes about a set of texts. Agents assign scores to themselves based on dictionary matches and other information, and a master controller combines the genes of the top scoring agents to create the next generation of agents. Over multiple generations, these agents evolve toward desired alignments, in a way that is similar to dog breeding or other processes of artificial selection among biological organisms. The system I have designed is free, open source and easy to use, allowing a researcher to select population sizes, mutation rates, scoring mechanisms and other variables to suit any particular alignment project. This software is also made to run on nearly any device, including cluster computers (e.g. the Leiden ALICE cluster), personal computers, mobile phones, and even Raspberry Pi and other single board computers.

</details>

### 5 Nov 2021

<details><summary>Full Stack Language Apps from the Bottom Up: Custom Online Portals for Humanities Research Using Linux, Python, Django & other Open Source Tools
</summary>

[LUCDH lunchtime speaker series](https://www.universiteitleiden.nl/en/events/2021/11/lucdh-lunchtime-speaker-series-christopher-handy)

![LUCDH](https://openphilology.eu/media/pages/partners/1327078252-1625255917/lucdhweb.png)
Join us for the LUCDH lunchtime talk presented by Dr. Christopher Handy on Wednesday, 3 November at 12:00 – 13:00.

Location: on-campus in the Digital Lab P.J. Veth 1.07 or online via Kaltura Live Rooms.

Christopher Handy will provide an overview of the major components he uses in his Digital Humanities course at Leiden University, ‘Constructing Digital Language Toolkits’. Now in its fourth iteration, the course helps bridge the gap between traditional humanities language research and web technologies.

Students with no prior background in software design learn to combine general purpose computing resources to create professional quality language toolkits for their specific research needs. Past projects created for the course include online multilingual dictionaries, language tagging engines, educational games, and various other useful applications.

This system places an emphasis on practical methods for bringing existing research projects to the digital realm quickly and easily. The modular design of this stack is especially useful for creating and maintaining dynamic solutions for low resource languages, for which specialized software is often limited or unavailable within the mainstream market.

To Register: Please email: lucdh@hum.leidenuniv.nl
We very much hope that you can join this live event in the Digital Lab in P.J. Veth 1.07. However, we will also be live-streaming on Kaltura, so please let us know if you will be attending in person or would like Kaltura Live Room login details.

</details>
