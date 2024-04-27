from django.shortcuts import render

# Create your views here.
def cert_view(request):
    return render(request, 'cert/hajar.html', {})
def home(request):
    return render(request, 'home.html', {})
def signature_view(request):
    return render(request, 'signature/sign.html', {})
def verification_view(request):
    return render(request, 'verification/ver.html', {})