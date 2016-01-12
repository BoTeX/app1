from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainPage, name='main'),
    url(r'^sellPage/$', views.sellPage, name='sell'),
    url(r'^buyPage/$', views.buyPage, name='buy'),
    url(r'^estate/$', views.estate, name='estate'),
    url(r'^transport/$', views.transport, name='transport'),
    url(r'^electronics/$', views.electronics, name='electronics'),
    url(r'^stuff/$', views.stuff, name='stuff'),
    url(r'^services/$', views.services, name='services'),
    url(r'^item/(?P<pk>[0-9]+)/$', views.item_detail, name='item'),
]