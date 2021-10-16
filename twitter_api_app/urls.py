from django.contrib.auth import views
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


app_name = "twitter_api"


URLPattern=[
  path('',views.main,name="search")
]
