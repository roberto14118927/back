from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    re_path(r'^$', views.prospect_list),
    re_path(r'^(?P<pk>\d+)$', views.prospect_detail),
]