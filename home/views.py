from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Count
from bugs.models import Bug
from features.models import Feature


def index(request):
    """
    A view that renders a home (index) page
    """
    return render(request, 'home/index.html')


def graphs(request):
    return render(request, 'home/graphs.html')


def graph_data(request):
    todo_no = Bug.objects.filter(fix_status='ToDo').count()
    doing_no = Bug.objects.filter(fix_status='Doing').count()
    done_no = Bug.objects.filter(fix_status='Done').count()
    bug_labels = ['todo', 'doing', 'done']
    bug_count = [todo_no, doing_no, done_no]

    todo_no = Feature.objects.filter(phase_of_development='ToDo').count()
    doing_no = Feature.objects.filter(phase_of_development='Doing').count()
    done_no = Feature.objects.filter(phase_of_development='Done').count()
    feature_labels = ['todo', 'doing', 'done']
    feature_count = [todo_no, doing_no, done_no]

    features = Feature.objects.order_by('-upvote')[:5]
    upvote_labels = []
    upvote_count = []
    for feature in features:
        upvote_labels.append(feature.name)
        upvote_count.append(feature.upvote)

    bugs = Bug.objects.order_by('-views')[:5]
    view_labels = []
    view_count = []
    for bug in bugs:
        view_labels.append(bug.title)
        view_count.append(bug.views)

    data = {
        'bug_labels': bug_labels,
        'bug_count': bug_count,
        'feature_labels': feature_labels,
        'feature_count': feature_count,
        'upvote_labels': upvote_labels,
        'upvote_count': upvote_count,
        'view_labels': view_labels,
        'view_count': view_count,
    }
    return JsonResponse(data)
