from django.http import HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from subprocess import Popen, PIPE, STDOUT

import json

from .models import Dictionary
from .models import DictionaryEntry

index_template="demoapp/index.html"
external_template="demoapp/external.html"
search_template="demoapp/search.html"

#commandpath="../engine/pythontest.py"
commandpath="../engine/dictchk.py"

def index(request):
    template = index_template

    return render(request,template,{})

def search(request):
    template = search_template
    if request.POST:
        term1 = request.POST.get('term1')
        d = DictionaryEntry.objects.filter(term1=term1)
        context = { "matches" : d, }
        return render(request, template, context)
    return render(request,template,{})

def external(request):
    template = external_template
    if request.POST:
        text1 = request.POST.get('text1')
        text2 = request.POST.get('text2')

        if request.POST.get("d1"):
            dict1 = "on"
        else:
            dict1 = "off"

        if request.POST.get("d2"):
            dict2 = "on"
        else:
            dict2 = "off"

        #command = ["python", commandpath]
        command = ["python", commandpath, text1, text2, dict1, dict2]

        process = Popen(command, stdout=PIPE, stderr=STDOUT)
        output = process.stdout.read()

        exitstatus = process.poll()

        if (exitstatus==0):
            result = str(output.decode("utf-8"))
        elif (exitstatus==None):
            result = str(output.decode("utf-8"))
        else:
            result = "No data."

        context = { "output" : str(result), }
        return render(request, template, context)
    return render(request,template,{})

