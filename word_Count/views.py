from django.http import HttpResponse
from django.shortcuts import render
import operator

def homePage(request):
    return render(request, 'home.html', {'hithere': 'Welcome To Sandeep\'s word count Website', 'textField': 'enter '
                                                                                                               'text '
                                                                                                               'here:'})


def count(request):
    word = request.GET['fulltext']
    c = word.split()

    wordDicyionery = {}

    for words in c:
        if words in wordDicyionery:
            wordDicyionery[words] += 1
        else:
            wordDicyionery[words] = 1

    sortedWords = sorted(wordDicyionery.items(), key=operator.itemgetter(1), reverse=True)
    print(sortedWords)

    return render(request, 'count.html', {'fulltext': word, 'count': len(c), 'wordDictionery': sortedWords})

def about(request):
    return render(request, 'about.html')