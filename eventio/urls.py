from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from accounts.views import register_user
from events.views import index, event_detail, event_add, event_edit, event_register

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^event/add/$', event_add, name='event_add'),
    url(r'^event/(?P<pk>\d+)/$', event_detail, name='event'),
    url(r'^event/(?P<pk>\d+)/register/$', event_register, name='event_register'),
    url(r'^event/(?P<pk>\d+)/edit/$', event_edit, name='event_edit'),
    url(
        r'^login/$', login,
        {'template_name': 'accounts/login.html'}, name='login'
    ),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', register_user, name='register'),
]
