from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView 

# Create a new class that redirects the user to the vote page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(selfself,request, user):
        return '/vote/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'swevote.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('swevoteapp.urls', namespace="swevoteapp")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^vote/', include('swevoteapp.urls', namespace="swevoteapp")),
        #Add in this url pattern to override the default pattern in accounts.
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    #url(r'^accounts/login/$', MyLoginView.as_view(), name = 'login_completed'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)

