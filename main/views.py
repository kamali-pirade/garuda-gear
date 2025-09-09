from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Garuda Gear',
        'name': 'Lessyarta Kamali Sopamena Pirade',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)