from django.shortcuts import render

def index(request):
    context = {
        'app_name': 'My E-Commerce App',
        'your_name': 'Geordie Vannese',
        'class': 'PBD KKI',
    }
    return render(request, 'main/index.html', context)
