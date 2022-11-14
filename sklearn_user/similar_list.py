from django.db.models import Q
from django.shortcuts import get_object_or_404
import os

from numpy import append

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()
from pybo.models import Similar,Maincont

class Similar_query:
    def __init__(self, user):
        self.user=user

    def my_similar(self):

        similar2 = Similar.objects.values_list('maincont').distinct()
        similar3 = similar2.filter(author__username__icontains=self.user).order_by('-similar')


        lists=list(similar3)

        similar_list= []

        for v in lists:
            similar_list.append(v[0])

        query = Maincont.objects.filter(id=similar_list[0])

        for i in similar_list:
            query = query | Maincont.objects.filter(id=i)
            #query.save()

        return query