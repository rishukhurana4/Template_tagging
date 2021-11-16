from django.conf.urls import url
from New_app import views

urlpatterns = [

url(r'^$',views.index,name='index'),
]
