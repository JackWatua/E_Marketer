from django.urls import path
from business_profile.views import show_profile
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path ("<str:name>/", show_profile, name = "profiles"),\
]

if settings.DEBUG: 
    urlpatterns += static (settings.MEDIA_URL, \
        document_root = settings.MEDIA_ROOT)