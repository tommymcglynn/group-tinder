from web.services import fake_service
from web.models import Person

print 'start'
for i in range(0, 100):
    print 'start iteration'
    person = Person.objects.random()
    fake_service.create_fake_judgements(person, 10)
    print 'end iteration'

print 'end'
