from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from authenticator.views import signUp, signIn


urlpatterns  = [
    path ("signup/", signUp, name = "sign_up"),\
    path("signin/", signIn, name = "sign_in")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, \
        document_root = settings.MEDIA_ROOT)