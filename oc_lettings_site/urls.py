from django.contrib import admin
from django.urls import include
from django.urls import path

from . import views


"""
This module defines the URL patterns for the main OC Lettings Site project.

@var urlpatterns: List of URL patterns mapping URLs to project-level views and included app URLs.
"""


def division_by_zero():
    return 1 / 0


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('test_sentry', division_by_zero)
]
