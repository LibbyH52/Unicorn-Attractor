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
    of all feature requests and render
    them to the template 'allfeatures.html.
    """
    features = Feature.objects.order_by('-posted_on').all()
    paginator = Paginator(features, 5)
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
    return render(request, "features/featuredescription.html", {"feature": feature, 'comments': comments})


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
    feature = get_object_or_404(Feature, pk=pk)
    if request.user == feature.requested_by:
        if request.method == "POST":
            form = AddFeatureForm(request.POST, instance=feature)
            if form.is_valid():
                form.save()
                return redirect('get_features')
        else:
            form = AddFeatureForm(instance=feature)
    else: 
        form = AddFeatureForm()
        messages.info(request, 'You do not have permission to edit this feature.')
    return render(request, "features/addfeature.html", {"form": form})


@login_required()
def add_feature_comment(request, pk):
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
    return render(request, "features/addfeaturecomment.html", {"form":form})   

@login_required()
def edit_feature_comment(request, pk):
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
        return render(request, "features/addfeaturecomment.html", {"form": form})
    else:
        messages.info(request, 'Only the author of a comment has permission to edit it.')
        form = AddFeatureCommentForm()
    return render(request, "features/addfeaturecomment.html", {"form":form})

@login_required()
def delete_feature_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    feature = comment.feature
    if request.user == comment.author:
        comment.delete()
        messages.success(request, 'This comment has been deleted.')
    else:
        messages.info(request, 'Only the author of a comment had permission to delete it.')
    return redirect('feature_description', pk=feature.pk)
   