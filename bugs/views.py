from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from .models import Bug, Comment
from .forms import AddBugForm, AddCommentForm


@login_required()
def show_bugs(request):
    """
    This view will return a list of all
    bugs in date order and display them on the
    'allbugs' template.
    """
    bugs = Bug.objects.order_by('-posted_on').all() 
    return render(request, 'bugs/allbugs.html', {'bugs':bugs})

@login_required()
def bug_description(request, pk):
    """
    This view allows a user to click on a particular
    bug to find out more details about it and add a
    comment
    """
    bug = get_object_or_404(Bug, pk=pk)
    bug.views += 1
    bug.save()
    form = AddCommentForm()
    comments = Comment.objects.order_by('-created_on').all() 
    return render(request, "bugs/bugdescription.html", {"bug":bug, "form":form, 'comments':comments})

@login_required()
def add_bug(request):
    """
    Create a view that allows a user to submit 
    or edit a bug report
    """
    if request.method =="POST":
        form = AddBugForm(request.POST or None)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug.save()
        return redirect(show_bugs)
    else:
        form = AddBugForm()
    return render(request, "bugs/addbug.html", {"form":form})


@login_required()
def add_comment(request):
    """
    Create a view that allows a user to comment 
    on a particular bug.
    """
    if request.method =="POST":
        form = AddCommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.bug = comment.bug
            comment.save()
        return redirect(bug_description, pk=pk)
    else:
        form = AddCommentForm()
    return render(request, "bugs/bugdescription.html", {"bug":bug, "form":form, 'comments':comments})



