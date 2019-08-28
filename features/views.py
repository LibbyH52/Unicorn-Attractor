from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,  get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Feature, Comment
from .forms import AddFeatureForm, AddFeatureCommentForm


@login_required()
def get_features(request):
    """
    A view that returns a list
    of all feature requests and renders
    them to the template 'allfeatures.html.
    Pagination displays eight features per
    page.
    """
    features = Feature.objects.order_by('-posted_on').all()
    paginator = Paginator(features, 8)
    page = request.GET.get('page')
    features = paginator.get_page(page)
    return render(request, 'features/allfeatures.html', {'features': features})


@login_required()
def feature_description(request, pk):
    """
    This view allows a user to click on a particular
    feature to find out more details about it and add a
    comment
    """
    feature = get_object_or_404(Feature, pk=pk)
    feature.save()
    comments = Comment.objects.filter(feature=feature)
    return render(request, "features/featuredescription.html",
                  {
                    "feature": feature,
                    'comments': comments
                  })


@login_required()
def new_feature(request):
    """
    A view that renders a form to allow
    a user to request a feature.
    """
    if request.method == "POST":
        form = AddFeatureForm(request.POST)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.requested_by = request.user
            feature.save()
            return redirect('get_features')
    else:
        form = AddFeatureForm()
    return render(request, 'features/addfeature.html', {'form': form})


@login_required()
def edit_feature(request, pk):
    """
    A view allows the user who requested
    the feature to edit it. Other users who
    try to access this functionality using
    the url will be redirected to a blank
    form where they can add a new feature.
    """
    feature = get_object_or_404(Feature, pk=pk)
    if request.user == feature.requested_by:
        if request.method == "POST":
            form = AddFeatureForm(request.POST, instance=feature)
            if form.is_valid():
                form.save()
                return redirect('feature_description', pk=feature.pk)
        else:
            form = AddFeatureForm(instance=feature)
        return render(request, "features/addfeature.html", {"form": form})
    else:
        form = AddFeatureForm()
        messages.info(request,
                      'You do not have permission to edit this feature.')
    return redirect('new_feature')


@login_required()
def delete_feature(request, pk):
    """
    A view that allows the user who requested
    the feature to delete it.
    """
    feature = get_object_or_404(Feature, pk=pk)
    if request.user == feature.requested_by:
        feature.delete()
        messages.success(request, 'This feature has been deleted.')
    else:
        messages.info(request,
                      'You do not have permission to delete this feature.')
    return redirect('get_features')


@login_required()
def add_feature_comment(request, pk):
    """
    A view that allows a logged in user to
    comment on a feature request.
    """
    feature = get_object_or_404(Feature, pk=pk)
    if request.method == "POST":
        form = AddFeatureCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.feature = feature
            comment.save()
            return redirect('feature_description', pk=feature.pk)
    else:
        form = AddFeatureCommentForm()
    return render(request, "features/addfeaturecomment.html", {"form": form})


@login_required()
def edit_feature_comment(request, pk):
    """
    A view allows the user who requested
    the feature to edit it. Other users who
    try to access this functionality using
    the url will be redirected to a blank
    form where they can add a new comment.
    """
    comment = get_object_or_404(Comment, pk=pk)
    feature = comment.feature
    if request.user == comment.author:
        if request.method == "POST":
            form = AddFeatureCommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('feature_description', pk=feature.pk)
        else:
            form = AddFeatureCommentForm(instance=comment)
        return render(request, "features/addfeaturecomment.html",
                      {"form": form})
    else:
        messages.info(request,
                      'You do not have permission to edit this comment.')
        form = AddFeatureCommentForm()
    return redirect('add_feature_comment', pk=feature.pk)


@login_required()
def delete_feature_comment(request, pk):
    """
    A view allows the user who wrote
    the comment to delete it.
    """
    comment = get_object_or_404(Comment, pk=pk)
    feature = comment.feature
    if request.user == comment.author:
        comment.delete()
        messages.success(request,
                         'This comment has been deleted.')
    else:
        messages.info(request,
                      'You do not have permission to delete this comment.')
    return redirect('feature_description', pk=feature.pk)
