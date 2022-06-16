from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
import urllib.request
# Create your views here.


@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=5ad0c5a5faddb06448ee5d671c79f8d9').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),

        }
    else:
        city = ''
        data = []
    return render(request, 'index.html', {'city': city, 'data': data})