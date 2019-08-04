from django.shortcuts import HttpResponse, render
import operator

def home(request):
    return render(request, 'index.html')
def count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            # increase
            worddictionary[word]+=1
        else:
            # add to the dictionary
            worddictionary[word]=1
    # So that the words are printed in order that highest appearing words first
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'fulltext': fulltext, 'count':len(wordlist),'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')
