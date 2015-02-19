from django.shortcuts import render_to_response, render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import *

def show_index(request):
    topicList = Topic.getTopics(request.user)
    paginator = Paginator(topicList, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)

    return render(request, 'tinybbs/index.html', {
        "topics":topics,
    })

def show_topic(request,url):
    targetTopic = get_object_or_404(Topic, url=url)

