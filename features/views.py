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

  
