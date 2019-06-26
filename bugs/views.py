from django.shortcuts import render
from .models import Bug, Comment

def show_bugs(request):
    """
    This view will return a list of all
    bugs in date order and display them on the
    'allbugs' template.
    """
    bugs = Bug.objects.order_by('-posted_on').all() 
    return render(request, 'bugs/allbugs.html', {'bugs':bugs})


