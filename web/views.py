from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from models import Person
from .forms import PersonForm

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
