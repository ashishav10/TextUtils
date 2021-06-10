#   Author: Ashish Vaishnav

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def remove_punc(djtext):
    analyzed = ''
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in djtext:
        if char not in punctuations:
            analyzed += char
    return analyzed

def cap_first(djtext):
    return djtext.title()

def space_remove(djtext):
    analyzed = ''
    for index, char in enumerate(djtext):
        if not(djtext[index] == ' ' and djtext[index + 1] == ' '):
            analyzed += char
    return analyzed

def newline_remove(djtext):
    
    djtext = djtext.replace("\n", "")
    djtext = djtext.replace("\r", "")
    print(djtext)
    return djtext

def char_count(djtext):
    return djtext + " " + str(len(djtext))

def analyze(request):
    # By default, GET request is used. It is used for non-sensitive data because in the GET request, the entered data is shown in the URL. It also has restriction on the length.

    # For sensitive data like passwords, PINs, we use POST request. Data is sent in the message body and not in the URL. There not restrictions on the length of the data.
    
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc')
    capfirst = request.POST.get('capfirst')
    spacesremove = request.POST.get('spacesremove')
    newlineremove = request.POST.get('newlineremove')
    charcount = request.POST.get('charcount')
    
    actions = [removepunc, capfirst, newlineremove, charcount, spacesremove]

    params = {'actual_text': djtext}
    if removepunc:
        analyzed = remove_punc(djtext)
        # djtext = analyzed
        params['analyzed_text'] = djtext = analyzed

    if capfirst:
        analyzed = cap_first(djtext)
        params['analyzed_text'] = djtext = analyzed

    if spacesremove:
        analyzed = space_remove(djtext)
        params['analyzed_text'] = djtext = analyzed

    if newlineremove:
        analyzed = newline_remove(djtext)
        params['analyzed_text'] = djtext = analyzed

    if charcount:
        analyzed = char_count(djtext)
        params['analyzed_text'] = analyzed

    if not any(actions):
        return HttpResponse('Please toggle at least one checkbox.')
    return render(request, 'analyze.html', params)
