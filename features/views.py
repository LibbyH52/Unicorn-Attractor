from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Feature


def get_features(request):
    """
    A view that returns a list
    of all feature requests and render
    them to the template 'allfeatures.html.
    """
    features = Feature.objects.order_by('-posted_on').all()
    return render(request, 'features/allfeatures.html', {'features': features})


def feature_details(request, pk):
    """
    A view that returns details of
    a single feature based on the primary key
    and renders it to the 'featuredetails.html'
    template. If the feature is not found a 404
    error will be returned.
    """
    feature = get_object_or_404(Feature, pk=pk)
    views += 1
    upvote += 1
    feature.save()
    return render(request, 'featuredetails.html', {'feature': feature})
