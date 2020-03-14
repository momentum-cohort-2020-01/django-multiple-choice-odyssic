from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Deck, Card
from .forms import DeckForm, CardForm
from django.contrib.auth import authenticate, login
from users.models import User
import random
from django import template
from django.views.decorators.http import require_http_methods, require_POST


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            redirect("home")
        else:
            return render("Account is not active")
            ...
    else:
        return render('Nope. Invalid Login Credentials')

# @login_required


def index(request):
    users = User.objects.all()
    decks = Deck.objects.all()

    return render(request, "core/index.html", {'users': users, 'decks': decks})

# defines deck by subject, returns all cards in that deck


def flashcards(request, pk):
    deck = Deck.objects.get(pk=pk)
    cards = deck.cards.all().order_by('?')

    return render(request, "core/flashcards.html", {'deck': deck, 'cards': cards, 'pk': pk})


def delete_deck(request, pk):
    deck = Deck.objects.get(Deck, pk=pk)
    deck.delete()
    return redirect('home')


def add_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save()
            return redirect("add_card")
    else:
        form = DeckForm()
    return render(request, 'core/add_deck.html', {'form': form})


def add_card(request, pk):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save()
            return redirect("home")
    else:
        form = DeckForm()
    return render(request, 'core/add_card.html', {'form': form, 'pk': pk})


@require_POST
def edit_card(request, pk):
    form = CardForm(request.POST)
    if form.is_valid():
        card = form.save()
        return redirect("flashcards")
    else:
        form = CardForm()
    return render(request, 'core/edit_card.html', {'form': form, 'pk': pk})


def delete_card(request, pk):
    card = Card.objects.get(Card, pk=pk)
    card.delete()
    return redirect('flashcards')

# @register.filter
# def shuffle(cards):
#     shuffled_cards = list(cards)[:]
#     random.shuffle(shuffled_cards)
#     return shuffled_cards

# def add_card()
