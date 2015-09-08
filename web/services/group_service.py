from web.models import Judgement, Match, Group
from django.core.exceptions import ObjectDoesNotExist

def index(positive_judgement):
    if not positive_judgement.ruling:
        print 'This is not a positive ruling'
        return
    # Are these 2 now a match?
    try:
        matched_judgement = Judgement.objects.get(judge=positive_judgement.judged, judged=positive_judgement.judge, ruling=True)
    except ObjectDoesNotExist:
        print 'Not a match'
        return
    match = Match.objects.get_existing(positive_judgement.judge, positive_judgement.judged)
    if match:
        print 'Found existing match: %s, %s' % (match.initiated, match.agreed)
    else:
        match = Match(initiated=positive_judgement.judged, agreed=positive_judgement.judge)
        print 'Found new match: %s, %s' % (match.initiated, match.agreed)
        match.save()

    # Do these 2 have any matches in common, to create a group?
    person_a = match.initiated
    person_b = match.agreed
    for match in Match.objects.filter(initiated=person_a):
        person_c = match.agreed
        common_match = Match.objects.get_existing(person_b, person_c)
        if common_match:
            get_or_create_group(person_a, person_b, person_c)
    for match in Match.objects.filter(agreed=person_a):
        person_c = match.initiated
        common_match = Match.objects.get_existing(person_b, person_c)
        if common_match:
            get_or_create_group(person_a, person_b, person_c)

def get_or_create_group(a, b, c):
    group = Group.objects.get_existing(a, b, c)
    if group:
        print 'Found existing group: %s, %s, %s, %s' % (a, b, c, group)
        return group
    group = Group.objects.create(a, b, c)
    print 'Found new group: %s, %s, %s, %s' % (a, b, c, group)
    return group
