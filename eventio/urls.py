from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from accounts.views import register_user
from events.views import index, event_detail, event_add, event_edit, event_delete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='home'),
    url(r'^event/(?P<pk>\d+)/$', event_detail, name='event'),
    url(r'^event/add/$', event_add, name='event_add'),
    url(r'^event/(?P<pk>\d+)/delete/$', event_delete, name='event_delete'),
    url(r'^event/(?P<pk>\d+)/edit/$', event_edit, name='event_edit'),
    url(r'^login/$', login,
        {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^sign-up/$', register_user, name='signup'),
]
