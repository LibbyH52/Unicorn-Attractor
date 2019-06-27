from django.shortcuts import render, get_object_or_404
from .models import Bug, Comment

def show_bugs(request):
    """
    This view will return a list of all
    bugs in date order and display them on the
    'allbugs' template.
    """
    bugs = Bug.objects.order_by('-posted_on').all() 
    return render(request, 'bugs/allbugs.html', {'bugs':bugs})

def bug_description(request, pk):
    """
    This view allows a user to click on a particular
    bug to find out more details about it and add a
    comment
    """
    bug = get_object_or_404(Bug, pk=pk)
    bug.views += 1
    bug.save()
    return render(request, "bugs/bugdescription.html", {"bug":bug})

