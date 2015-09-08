from web.models import Person

def get_random_person(not_this_person):
    person = None
    while person is None:
        p = Person.objects.random()
        if p.pk is not not_this_person.pk:
            person = p
    return person
