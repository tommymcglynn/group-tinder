from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from models import Person, User, Judgement
from .forms import PersonForm
from services import group_service, fake_service, person_service
from django.db import IntegrityError

def home(request):
    user = request.user
    return render_to_response('home.html', {'user': user})

def profile(request):
    if not request.user.is_active:
        return redirect('/accounts/login')
    user = request.user
    try:
        person = Person.objects.get(user=user)
    except ObjectDoesNotExist:
        person = None

    if request.method == 'POST':
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            person = form.save(commit=False)
            person.user = user
            person.save()
            # redirect to a new URL:
            return redirect('/accounts/profile/')
    # if a GET (or any other method) we'll create a blank form
    elif person is None:
        form = PersonForm()
    elif request.GET.get('edit'):
        form = PersonForm(instance=person)
    else:
        form = None

    return render_to_response('profile.html', {'user': user, 'person': person, 'form': form}, context_instance=RequestContext(request))

def people(request):
    if not request.user.is_active:
        return redirect('/accounts/login')
    user = request.user
    person = user.person
    if person is None:
        return redirect('/accounts/profile/?edit=true')

    if request.method == 'POST':
        ruling = 'yes' in request.POST
        person_judged = Person.objects.get(pk=request.POST['person_pk'])
        judgement = Judgement(judge=person, judged=person_judged, ruling = ruling)
        try:
            judgement.save()
        except IntegrityError:
            pass
        if ruling:
            group_service.index(judgement)

    suggested_person = person_service.get_random_person(person)
    return render_to_response('people.html', {'user': user, 'suggested_person': suggested_person}, context_instance=RequestContext(request))

def groups(request):
    if not request.user.is_active:
        return redirect('/accounts/login')
    user = request.user
    person = user.person
    if person is None:
        return redirect('/accounts/profile/?edit=true')

    groups = person.group_set.all()
    return render_to_response('groups.html', {'user': user, 'groups': groups})

def create_fake_people(request):
    fake_service.create_fake_people()
