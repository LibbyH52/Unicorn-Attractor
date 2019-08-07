from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,  get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Feature
from .forms import AddFeatureForm


@login_required()
def get_features(request):
    """
    A view that returns a list
    of all feature requests and render
    them to the template 'allfeatures.html.
    """
    features = Feature.objects.order_by('-posted_on').all()
    paginator = Paginator(features, 4)
    page = request.GET.get('page')
    features = paginator.get_page(page)
    return render(request, 'features/allfeatures.html', {'features': features})


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
    if request.method == "POST":
        form = AddFeatureForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('get_features')
    else:
        form = AddFeatureForm(instance=feature)
    return render(request, "features/addfeature.html", {"form": form})

