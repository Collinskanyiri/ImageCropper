from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='mainPage'), 
    # url(r'^$', views.photo_list, name="photo_list"),
    path('search/', views.search_images, name='searchPage'), 
    path('location/<location>/', views.view_by_location, name='locationPage'), 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)