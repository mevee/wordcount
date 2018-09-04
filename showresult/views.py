from django.shortcuts import render
from . import templates
import operator

# Create your views here.
def showresult(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()
    worddictionary ={}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedword = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse= True)
    return render(request,'result.html',{'result':fulltext,'wordcount':len(wordlist) ,'worddictionary':sortedword})

def home(request):
    return render(request,'showresult/home.html',{})

def about(request):
    return render(request,'showresult/aboutus.html',{})
