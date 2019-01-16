from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from . views import emailview, successview

app_name = 'contacts'

urlpatterns = [
	path('email/', emailview, name='email'),
	path('success/', successview, name="success"),
]	