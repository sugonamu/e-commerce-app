from django.shortcuts import render

def info_view(request):
    context = {
        'app_name': 'E-Commerce Shop', 
        'your_name': 'Will',     
        'your_class': 'KKI',  
    }
    return render(request, 'main1.html', context)
