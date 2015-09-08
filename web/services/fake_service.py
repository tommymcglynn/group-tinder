from web.models import Person, User, Judgement
from random import getrandbits
import person_service, group_service
from django.db import IntegrityError

def create_fake_people():
    user_group = 'alpha'
    for i in range(0, 100):
        name = 'fake_user_%s_%s' % (user_group, i)
        user = User(username=name, email='%s@email.com'%(name), password='password')
        user.save()
        person = Person.objects.create_random(user)
        person.save()

def create_fake_judgements(person, count):
    for i in range(0, count):
        ruling = bool(getrandbits(1))
        random_person = person_service.get_random_person(person)
        judgement = Judgement(judge=person, judged=random_person, ruling=ruling)
        try:
            judgement.save()
        except IntegrityError:
            judgement = Judgement.objects.get(judge=person, judged=random_person)
            judgement.ruling = ruling
            judgement.save()
        if judgement.ruling:
            group_service.index(judgement)
