from django.contrib import admin
from django.urls import path
from web import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home.homeview, name='homeview'),
    path('entreprise', views.entreprise.entreprise, name='entreprise'),
    path('mission', views.home.mission, name='mission'),
    path('epreuve', views.home.epreuve, name='epreuve'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)