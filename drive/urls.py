from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    re_path(r'^$', views.driveList.as_view()),
    re_path(r'^(?P<id>\d+)$', views.driveDetail.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)