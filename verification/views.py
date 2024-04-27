from django.shortcuts import render,redirect
#from django.contrib.auth import authenticate, login, logout
#from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm

#def login_user(request):
#	if request.method == "POST":
#		username = request.POST['username']
#		password = request.POST['password']
#		user = authenticate(request, username=username, password=password)
#		if user is not None:
#			login(request, user)
#			return redirect('home')
#		else:
#			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
#			return redirect('login')	
#
#
#	else:
#		return render(request, 'authenticate/login.html', {})
#
#def logout_user(request):
#	logout(request)
#	messages.success(request, ("You Were Logged Out!"))
#	return redirect('home') 


# Create your views here.
def verification_view(request):
    return render(request, 'verification/ver.html', {})
def cert_view(request):
    return render(request, 'cert/hajar.html', {})
def home(request):
    return render(request, 'home.html', {})
def signature_view(request):
    return render(request, 'signature/sign.html', {})
def paiement_view(request):
    return render(request, 'paiement/payment.html', {})
