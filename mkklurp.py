#!/usr/bin/env python3

import sys, os, sh
import subprocess

basepath = os.getcwd()
venvname = "demovenv"
projectname = "demoproject"
appname = "demoapp"

if len(sys.argv) > 1:
    venvname = sys.argv[1]

if len(sys.argv) > 2:
    projectname = sys.argv[2]

if len(sys.argv) > 3:
    appname = sys.argv[3]

venvpath = os.path.join(basepath, venvname)

print (venvname, projectname, appname)

subprocess.run(["python3", "-m", "venv", venvname])

staticdir = os.path.join(venvpath, "static")
mediadir = os.path.join(venvpath, "media")
enginedir = os.path.join(venvpath, "engine")
rundir = os.path.join(venvpath, "run")

os.mkdir( staticdir )
os.mkdir( mediadir )
os.mkdir( enginedir )
os.mkdir( rundir )

os.chdir(venvpath)
sh.sh('-c', '. bin/activate; pip3 install django; pip3 install gunicorn')
projectstring = 'django-admin startproject ' + projectname

sh.sh('-c', projectstring)
interfacename = "interface"
enginename = "engine"

os.rename(projectname, interfacename)
projectpath = os.path.join(venvpath, interfacename)
enginepath = os.path.join(venvpath, enginename)

os.chdir(projectpath)
appstring = 'python3 manage.py startapp ' + appname
sh.sh('-c', appstring)

#os.chdir("/home/handyc/klurp")
#os.chdir(correct_klurp_directory_set_at_install")
os.chdir(basedir)
copystring = 'cp samplefiles/project/*.py ' + projectpath
copystring2 = 'cp samplefiles/engine/* ' + enginepath
copystring3 = 'cp samplefiles/engine/* ' + enginepath
sh.sh('-c', copystring)
sh.sh('-c', copystring2)
sh.sh('-c', copystring3)
print(copystring)
print(copystring2)
print(copystring3)


#

# copy the template files

#cp samplefiles/project/*.py projectpath
#cp samplefiles/engine/* enginepath
#cp samplefiles/engine/* enginepath

# subprocess.run(["ls", "-l"])
# exit with message
# print ('thanks for using klurp')
# print ('exited at: 00 00 00 on 00 00 00 0000 at location 00,00,00')
# coords

#cp ~/scripts/samplefiles/project/*.py $projectpath
#cp ~/scripts/samplefiles/engine/* $enginepath
#cp -r ~/scripts/samplefiles/engine/* $enginepath
