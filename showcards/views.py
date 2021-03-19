from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import Cards,TempCards
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random


# Create your views here.
@login_required(login_url='/login')
def ShowCards(request):
	getCards = Cards.objects.filter()
	getUsers = User.objects.filter(is_superuser=False)
	getCards__ = Cards.objects.filter(status=1)
	cards_ = []
	for c in getCards:
		cards_.append(c.id)
	users_ =[]
	for u in getUsers:
		users_.append(u.id)
	random.shuffle(cards_)
	x=0 
	y=52
	AssignedCards = []
	for i in range(x,y,13):
		x=i
		AssignedCards.append(cards_[x:x+13])
	if 'add_item' in request.POST:
		val_ = request.POST['val_']
		getCards__ = Cards.objects.filter(status=1)
		doUpdate = Cards.objects.get(id=val_)
		doUpdate.status = 1
		print(doUpdate)
		doUpdate.save()
		return render(request,'showcards/temppage.html',{'getCards__':getCards__})
	elif 'end_game' in request.POST:
		for m in getCards:
			if m.status == 1:
				m.status = 0
				m.save()
	dict_ = {}
	for keys in users_:
		for value in AssignedCards:
			dict_[keys] = value

	return render(request,'showcards/main.html',{'getCards':getCards,'dict_':dict_,'getCards__':getCards__})

def registerPage(request):
		form = CreateUserForm()
		if request.method =='POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				print('po')
				user = form.save()
				username = form.cleaned_data.get('username')
				# group = Group.objects.get(name='customer')
				# user.groups.add(group)
				# Customer.objects.create(
				# 	user=user
				# )
				messages.success(request,'Account was created for ' + username )
				return redirect('login')
		context={'form':form}
		return render(request,'showcards/register.html',context)

def loginPage(request):
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user=authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('show_cards')
			else:
				messages.info(request,'Username or Password incorrect')

		context={}
		return render(request,'showcards/login.html',context)

def logoutUser(request):
	logout(request)
	return redirect('login')