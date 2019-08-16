from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
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
    paginator = Paginator(bugs, 5)
    page = request.GET.get('page')
    bugs = paginator.get_page(page)
    return render(request, 'bugs/allbugs.html', {'bugs' : bugs})


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
    return render(request, "bugs/bugdescription.html", {"bug":bug})

@login_required()
def add_bug(request):
    """
    Create a view that allows a user to submit 
    or edit a bug report
    """
    if request.method == "POST":
        form = AddBugForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug.save()
            return redirect('bug_description', pk=bug.pk)
    else:
        form = AddBugForm()
    return render(request, "bugs/addbug.html", {"form": form})

@login_required()
def edit_bug(request, pk=None):
    bug = get_object_or_404(Bug, pk=pk)
    if request.user == bug.author:
        if request.method == "POST":
            form = AddBugForm(request.POST, instance=bug)
            if form.is_valid():
                form.save()
                return redirect('bug_description', pk=bug.pk)
        else:
            form = AddBugForm(instance=bug)
        return render(request, "bugs/addbug.html", {"form": form})
    else:
        messages.info(request, 'Only the author can edit this bug.')
    return redirect('bug_description', pk=bug.id)


@login_required()
def add_comment(request, pk):
    """
    Create a view that allows a user to comment 
    on a particular bug.
    """
    bug = get_object_or_404(Bug, pk=pk)
    if request.method == "POST":
        form = AddCommentForm(request.POST)
    
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.bug = bug
            comment.save()
            return redirect('bug_description', pk=bug.pk)
    else:
        form = AddCommentForm()
    return render(request, "bugs/addcomment.html", {"form":form})


@login_required()
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    bug = comment.bug
    if request.user == comment.author:
        if request.method == "POST":
            form = AddCommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('bug_description', pk=bug.pk)
        else:
            form = AddCommentForm(instance=comment)
        return render(request, "bugs/addcomment.html", {"form": form})
    else:
        messages.info(request, 'Only the author of a comment has permission to edit it.')
        form = AddCommentForm()
    return render(request, "bugs/addcomment.html", {"form":form})


@login_required()
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    bug = comment.bug
    if request.user == comment.author:
        comment.delete()
    else:
        messages.info(request, 'Only the author of a comment had permission to delete it.')
    return redirect('bug_description', pk=bug.pk)