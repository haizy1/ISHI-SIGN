from django.shortcuts import render
import requests
import certifi

def home(request):
    result = None
    if request.method == 'POST':
        url = request.POST.get('url')
        result = check_ssl_certificate(url)
    return render(request, 'checker_app/checker.html', {'result': result})

def check_ssl_certificate(url):
    try:
        response = requests.get(url, verify=certifi.where())
        if response.ok:
            return {'message': "The SSL certificate is installed properly and trusted by browsers.", 'class': 'success'}
        else:
            return {'message': "The SSL certificate is not trusted by browsers.", 'class': 'error'}

    except requests.exceptions.SSLError:
        return {'message': "An SSL error occurred. Please check the SSL certificate installation.", 'class': 'error'}
    except requests.exceptions.RequestException as e:
        return {'message': "An error occurred: " + str(e), 'class': 'error'}
