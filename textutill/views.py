
# I create this-->

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name':'raja', 'place':'batun'}
    return render(request, 'index.html', params)

def about(request):
    return render(request,'about.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('checkbox','off')
    upper_case = request.POST.get('upper_case','off')
    newlineremover = request.POST.get('new_line_remover','off')
    remove_extra_space = request.POST.get('remove_extra_space','off')
    char_count = request.POST.get('char_count', 'off')

    if removepunc == 'on':
        punctuations = '''.,?!:<>;'"-()[]{}…—_/\@#$%^&*~`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if upper_case == 'on':
        temp = ""
        for char in djtext:
            temp = temp + char.upper()
        params = {'purpose':'Change to Upper Case','analyzed_text':temp}
        # return render(request,'analyze.html',params)
        djtext = temp
    if newlineremover == 'on':
        temp = ""
        for char in djtext:
            if(char != "\n" and char != "\r"):
                temp += char
        params = {'purpose':'Remove new lines', 'analyzed_text':temp}
        # return render(request,'analyze.html',params)
        djtext = temp
    if remove_extra_space == 'on':
        temp = ""
        for index, char in enumerate(djtext):
            if(djtext[index] == " " and djtext[index+1] == " "):
                pass
            else:
                temp += char
        params = {'purpose':'Remove extra spaces','analyzed_text':temp}
        # return render(request, 'analyze.html',params)
        djtext = temp
    if char_count == 'on':
        count = 0
        temp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for char in djtext:
            if(char in temp):
                count += 1
        params = {'purpose':'Character count','analyzed_text': count}
        # return render(request,'analyze.html',params)
        djtext = temp
    if(removepunc != 'on' and upper_case != 'on' and newlineremover != 'on' and remove_extra_space != 'on' and char_count != 'on'):
        return HttpResponse("<h1>Please select any operation and try again<h1>")
    return render(request, 'analyze.html', params)



def capitalizefirst(request):
    return HttpResponse('''capitalizefirst <br> <br> <button onclick = "history.back()" style = "padding: 10px 20px; background-color: #e5d7d4 ; color:black; border-radius: 10px; border: 2px solid black;   ">back</button>''')
def newlineremove(request):
    return HttpResponse('''newlineremove <br> <br> <button onclick = "history.back()" style = "padding: 10px 20px; background-color: #e5d7d4 ; color:black; border-radius: 10px; border: 2px solid black;   ">back</button>''')
def spaceremove(request):
    return HttpResponse('''spaceremove <br> <br> <button onclick = "history.back()" style = "padding: 10px 20px; background-color: #e5d7d4 ; color:black; border-radius: 10px; border: 2px solid black;   ">back</button>''')
def charcount(request):
    return HttpResponse('''charcount <br> <br> <button onclick = "history.back()" style = "padding: 10px 20px; background-color: #e5d7d4 ; color:black; border-radius: 10px; border: 2px solid black;   ">back</button>''')


