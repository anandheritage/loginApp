from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.core.urlresolvers import reverse
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
# Create your views here.

def login_view(request):
	form = LoginForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		#print form.cleaned_data['username']
		user = authenticate(username=username, password=password)
		login(request,user)
		return HttpResponseRedirect(reverse("home"))

	context = {'form':form}
	template = "login.html"
	return render(request,template,context)

@login_required(login_url='/login')
def home(request):
	context = {}
	template = "home.html"
	return render(request,template,context)

@login_required(login_url='/login')
def logout_view(request):
	if request.user.is_authenticated():
		logout(request)
	return HttpResponseRedirect(reverse('home'))