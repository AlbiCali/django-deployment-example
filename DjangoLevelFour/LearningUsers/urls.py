"""
Definition of urls for DjangoLevelFour.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from LearningUsers import views
import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
# admin.autodiscover()

# template tagging app_name variable
app_name = 'LearningUsers'


urlpatterns = [
    # Examples:
    #url(r'^$', app.views.home, name='home'),

    url(r'^Registration/', views.Register, name='Register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    

    ]

