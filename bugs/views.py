from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Bug, Comment
from .forms import AddBugForm, BugCommentForm


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
    form = BugCommentForm(request.POST or None)
    comments = Comment.objects.order_by('-posted_on').all() 
    bug = get_object_or_404(Bug, pk=pk)
    bug.views += 1
    bug.save()
    return render(request, "bugs/bugdescription.html", {"bug":bug, "form":form, 'comments':comments})

def add_bug(request):
    if request.method =="POST":
        form = AddBugForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect(request, "bugs/allbugs.html", {"bugs":bugs})
    else:
        form = AddBugForm()
        return render(request, "bugs/addbug.html", {"form":form})

def add_comment(request):
    if request.method =="POST":
        form = AddCommentForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, "bugs/bugdescription.html", {"bug":bug, "form":form, 'comments':comments})
    else:
        form = AddCommentForm()
    return render(request, "bugs/bugdescription.html", {"bug":bug, "form":form, 'comments':comments})



