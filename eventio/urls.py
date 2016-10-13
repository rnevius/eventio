from django.conf.urls import url
from django.contrib import admin
from events.views import index, event_detail, event_add

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='home'),
    url(r'^event/(?P<pk>\d+)/$', event_detail, name='event'),
    url(r'^event/add/$', event_add, name='event_add'),
]
