from django.shortcuts import render
import requests

def home(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('https://api.spacexdata.com/v4/capsules')
    geodata = response.json()
    return render(request, 'webapp/home.html', {
        'ip': len(geodata),

        })


