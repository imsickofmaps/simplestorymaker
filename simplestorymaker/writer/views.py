from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from models import Story, Role


def index(request):
    roles = Role.objects.order_by('name')
    context = {
        'text': "Hello, world. You're at the homepage.",
        'roles': roles,
    }
    return render(request, 'writer/index.html', context)


def latest(request):
    latest_story_list = Story.objects.order_by('-create_date')[:5]
    context = {
        'latest_story_list': latest_story_list,
    }
    return render(request, 'writer/latest.html', context)


def story(request, story_id):
    try:
        story = Story.objects.get(pk=story_id)
    except Story.DoesNotExist:
        raise Http404
    return render(request, 'writer/story.html', {'story': story})


def new(request):
    if (request.POST['reason'] != '' and request.POST['role'] != ''
            and request.POST['goal'] != ''):
        role = Role.objects.get(id=request.POST['role'])
        story = Story(reason=request.POST['reason'], role=role,
                      goal=request.POST['goal'], create_date=timezone.now())
        story.save()
        return HttpResponseRedirect(reverse('writer:story', args=(story.id,)))
    else:
        return HttpResponseRedirect(reverse('writer:index'))
