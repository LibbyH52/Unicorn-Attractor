from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from .models import Bug, Comment
from .forms import AddBugForm, AddBugCommentForm


@login_required()
def show_bugs(request):
    """
    This view will return a list of all
    bugs in date order and display them on the
    'allbugs' template. Pagination is used to
    display eight bugs per page.
    """
    bugs = Bug.objects.order_by('-posted_on').all()
    paginator = Paginator(bugs, 8)
    page = request.GET.get('page')
    bugs = paginator.get_page(page)
    return render(request, 'bugs/allbugs.html', {'bugs': bugs})


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
    comments = Comment.objects.filter(bug=bug)
    return render(request, "bugs/bugdescription.html",
                  {
                     'bug': bug, 'comments': comments
                   })


@login_required()
def add_bug(request):
    """
    Creates a view that allows a user to submit
    bug report
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
    """
    A view that allows the author of a bug report to
    edit it.
    """
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
        form = AddBugForm()
    return render(request, "bugs/addbug.html", {"form": form})


@login_required()
def add_bug_comment(request, pk):
    """
    This view allows a user to comment
    on a particular bug.
    """
    bug = get_object_or_404(Bug, pk=pk)
    if request.method == "POST":
        form = AddBugCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.bug = bug
            comment.save()
            return redirect('bug_description', pk=bug.pk)
    else:
        form = AddBugCommentForm()
    return render(request, "bugs/addbugcomment.html", {"form": form})


@login_required()
def edit_bug_comment(request, pk):
    """
    This view allows the author of a comment to
    edit it.
    """
    comment = get_object_or_404(Comment, pk=pk)
    bug = comment.bug
    if request.user == comment.author:
        if request.method == "POST":
            form = AddBugCommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('bug_description', pk=bug.pk)
        else:
            form = AddBugCommentForm(instance=comment)
        return render(request, "bugs/addbugcomment.html", {"form": form})
    else:
        messages.info(request,
                      'Only the author of a comment can edit it.')
        form = AddBugCommentForm()
    return render(request, "bugs/addbugcomment.html", {"form": form})


@login_required()
def delete_bug_comment(request, pk):
    """
    This view allows the author of a comment to
    delete it.
    """
    comment = get_object_or_404(Comment, pk=pk)
    bug = comment.bug
    if request.user == comment.author:
        comment.delete()
        messages.success(request, 'This comment has been deleted.')
    else:
        messages.info(request,
                      'Only the author of a comment can delete it.')
    return redirect('bug_description', pk=bug.pk)
