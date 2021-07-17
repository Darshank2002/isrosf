from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [

    path('', views.index, name='home'),
    path('rockets/', views.rockets, name='rockets'),

    path('missions/', views.missions, name='missions'),
    path('missions/<str:Type>/<str:code>/',
         views.missionPage, name='missionPage'),
    path('missions/<str:Type>/', views.missionsTemp, name='missionsTemp'),
    path('timeline/', views.timeline, name='timeline'),
    path('rockets/<str:code>', views.lv, name="lv"),
    path('spacecraft/', views.spacecraft, name='spacecraft'),
    path('news/', views.news, name="news"),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
