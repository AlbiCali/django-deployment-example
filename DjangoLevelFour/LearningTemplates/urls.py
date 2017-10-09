"""
Definition of urls for DjangoLevelFour.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from LearningTemplates import views
import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
# admin.autodiscover()

# template tagging app_name variable
app_name = 'LearningTemplates'


urlpatterns = [
    # Examples:
    #url(r'^$', app.views.home, name='home'),

    url(r'^$', views.index, name='index'),
    url(r'^other/$', views.other, name='other'),
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^',include('LearningUsers.urls')),

    ]
