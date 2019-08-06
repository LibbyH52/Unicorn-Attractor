from django.shortcuts import render


def index(request):
    """
    A view that renders a home (index) page
    """
    return render(request, 'home/index.html')
