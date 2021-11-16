import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','New_project.settings')

import django
django.setup()

import random
from New_app.models import AccessRecords,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Machine learning', 'Deep Learning', 'PYTHON', 'Data Mining']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()

        fake_url=fakegen.url()
        fake_name=fakegen.company()
        fake_date=fakegen.date()

        webpg=Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]
        acc_rec = AccessRecords.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("poplulating script")
    populate(20)
    print("populating complete")
