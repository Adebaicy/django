# -*- coding: utf-8 -*-

from django.urls import path

from blog import views

app_name="blog"

urlpatterns = [
    path("",views.blog),
    path('<int:iid>', views.story, name='det'),
    #generating automatic url from base id
    
    ]