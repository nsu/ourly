from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf.urls.defaults import *
from tastypie.api import Api
from timer.api import WorkSessionResource, UserResource
from django.contrib.auth.decorators import login_required


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Tastypie api
v1_api = Api(api_name='v1')
v1_api.register(WorkSessionResource())
v1_api.register(UserResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ourly.views.home', name='home'),
    # url(r'^ourly/', include('ourly.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login_required(TemplateView.as_view(template_name='home.html'))),
    (r'^api/', include(v1_api.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login',
    {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
)
