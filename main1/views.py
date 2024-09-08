from django.shortcuts import render

def info_view(request):
    context = {
        'app_name': 'E-Commerce Shop',  # Replace with the actual application name
        'your_name': 'Will',     # Replace with your actual name
        'your_class': 'KKI',   # Replace with your actual class
    }
    return render(request, 'main1/info.html', context)
