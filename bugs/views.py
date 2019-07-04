from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from .models import Bug, Comment
from .forms import AddBugForm, AddCommentForm


@login_required(login_url=reverse_lazy('login'))
def show_bugs(request):
    """
    This view will return a list of all
    bugs in date order and display them on the
    'allbugs' template.
    """
    bugs = Bug.objects.order_by('-posted_on').all() 
    return render(request, 'allbugs.html', {'bugs':bugs})

@login_required(login_url=reverse_lazy('login'))
def bug_description(request, pk):
    """
    This view allows a user to click on a particular
    bug to find out more details about it and add a
    comment
    """
    form = AddCommentForm(request.POST or None)
    comments = Comment.objects.order_by('-created_on').all() 
    bug = get_object_or_404(Bug, pk=pk)
    bug.views += 1
    bug.save()
    return render(request, "bugdescription.html", {"bug":bug, "form":form, 'comments':comments})

@login_required(login_url=reverse_lazy('login'))
def add_bug(request):
    """
    View that allows a user to submit a bug report
    """
    if request.method =="POST":
        form = AddBugForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect(request, "allbugs.html", {"bugs":bugs})
    else:
        form = AddBugForm()
        return render(request, "addbug.html", {"form":form})

@login_required(login_url=reverse_lazy('login'))
def add_comment(request):
    """
    View that allows a user to comment on 
    a particular bug.It will appear underneath the 
    the bug
    """
    if request.method =="POST":
        form = AddCommentForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, "bugdescription.html", {"bug":bug, "form":form, 'comments':comments})
    else:
        form = AddCommentForm()
    return render(request, "bugdescription.html", {"bug":bug, "form":form, 'comments':comments})



