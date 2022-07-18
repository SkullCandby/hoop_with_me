from django.shortcuts import render

def map(request):
    context = {}
    return render(request, 'map.html', context)