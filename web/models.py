from django.db import models
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from random import randint, getrandbits, choice


class PersonsManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('pk'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]

    def create_random(self, user):
        gender = Person.GENDERS[0][0] if bool(getrandbits(1)) else Person.GENDERS[1][0]
        stereotype = choice(Person.STEREOTYPES)[0]
        return Person(user=user, age=randint(13, 65), gender=gender, stereotype=stereotype)


class Person(models.Model):
    objects = PersonsManager()
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    STEREOTYPES = (
        (0, 'Jock'),
        (1, 'Hippie'),
        (2, 'Bro'),
        (3, 'Diva'),
        (4, 'Bookworm'),
        (5, 'Techie'),
        (6, 'Dancer'),
        (7, 'Emo'),
    )
    user = models.OneToOneField(User, primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDERS)
    stereotype = models.IntegerField(choices=STEREOTYPES)

    def __str__(self):
        return 'Person[pk=%s,age=%s,gender=%s,stereotype=%s]' % (self.pk, self.age, self.gender, self.stereotype)


class Judgement(models.Model):
    class Meta:
        unique_together = (("judge", "judged"),)
    judge = models.ForeignKey(Person, verbose_name='the person judging', related_name='%(app_label)s_%(class)s_made')
    judged = models.ForeignKey(Person, verbose_name='the person being judged', related_name='%(app_label)s_%(class)s_received')
    ruling = models.BooleanField('the value of the judgement')


class MatchesManager(models.Manager):
    def get_existing(self, a, b):
        match = None
        try:
            match = self.get(initiated=a, agreed=b)
            return match
        except ObjectDoesNotExist:
            pass
        try:
            match = self.get(agreed=a, initiated=b)
        except ObjectDoesNotExist:
            pass
        return match


class Match(models.Model):
    objects = MatchesManager()

    class Meta:
        unique_together = (("initiated", "agreed"),)

    initiated = models.ForeignKey(Person, verbose_name='Initiator of match', related_name='%(app_label)s_%(class)s_initiated')
    agreed = models.ForeignKey(Person, verbose_name='Matched in agreement', related_name='%(app_label)s_%(class)s_agreed')


class GroupsManager(models.Manager):
    def create(self, a, b, c):
        init_hash = self.get_hash(a, b, c)
        group = Group(init_hash=init_hash)
        group.save()
        group.people.add(a, b, c)
        return group

    def get_existing(self, a, b, c):
        init_hash = self.get_hash(a, b, c)
        try:
            existing = self.get(init_hash=init_hash)
            return existing
        except ObjectDoesNotExist:
            pass
        return None

    def get_hash(self, a, b, c):
        pks = sorted([a.pk, b.pk, c.pk])
        return hash('%s:%s:%s' % (pks[0], pks[1], pks[2]))


class Group(models.Model):
    objects = GroupsManager()

    init_hash = models.IntegerField(unique=True)
    people = models.ManyToManyField(Person)

    def __str__(self):
        return 'Group[init_hash=%s]' % (self.init_hash)
