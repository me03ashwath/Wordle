from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from game.models import Words

def homePage(request):
    context = {}
    return render(request, 'game/home.html', context)

def playGame(request):
    word = Words.objects.get(id=2)
    letters = ['A','D','L','T','P','V','W']
    context = {'word':word, 'max_guss':range(5), 'word_length':range(word.word_length), 'letters':letters}
    return render(request, 'game/game.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def addWords(request):

    words = list('apple brick crown dance eager flight ghost happy ivory jolly lemon magic ocean paint river slice trust upper visit yawn zeal agent beard chaos depth envoy flask grape heart icing joker kingf laugh monkey olive paper quick rogue smile today unite valid watch xray zebra agile board chair drill enter faith glory house index jetty lodge minor noise outer party quote rocket space thumb uncle value zone amber beach clown dream eagle fancy grant honor image joint kites lucky mimic nacho oasis parade quiz rumor stone track utter vixen wharf yeast zesty'.split())
    for word in words:
        try:
            Words.objects.create(word_length=len(word), word=word)
        except:
            pass