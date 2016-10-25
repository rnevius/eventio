from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from accounts.views import register_user
from events.views import index, event_detail, event_add

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^event/(?P<pk>\d+)/$', event_detail, name='event'),
    url(r'^event/add/$', event_add, name='event_add'),
    url(
        r'^login/$',
        auth_views.login,
        {'template_name': 'accounts/login.html'},
        name='login'
    ),
    url(r'^register/$', register_user, name='register'),
    url('^', include('django.contrib.auth.urls')),
]
