from django.shortcuts import render
from New_app import views
from New_app.models import AccessRecords, Webpage, Topic
# Create your views here.

def index(request):
    webpages_list = Webpage.objects.order_by('url')
    date_dict = {'access_records': webpages_list}
    return render(request,'New_app/index.html', context=date_dict)
