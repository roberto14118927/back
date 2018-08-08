from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from globalsettings import views

# router = routers.DefaultRouter()
# router.register(r'institution', views.InstitutionList)

urlpatterns = [
    re_path(r'^institution/$', views.InstitutionList.as_view()),
    re_path(r'^institution/(?P<pk>\d+)$', views.InstitutionDetail.as_view()),
    # ---------------------------------------------------------------------------------
    re_path(r'^educationtype/$', views.EducationTypeList.as_view()),
    re_path(r'^educationtype/(?P<pk>\d+)$', views.EducationTypeDetail.as_view()),
    # ---------------------------------------------------------------------------------
    re_path(r'^educationlevel/$', views.CatEducationLevelList.as_view()),
    re_path(r'^educationlevel/(?P<pk>\d+)$', views.CatEducationLevelDetail.as_view()),
    # ---------------------------------------------------------------------------------
    re_path(r'^educationarea/$', views.CatEducationAreaList.as_view()),
    re_path(r'^educationarea/(?P<pk>\d+)$', views.CatEducationAreaDetail.as_view()),
    # ---------------------------------------------------------------------------------
    re_path(r'^education/$', views.EducationList.as_view()),
    re_path(r'^education/(?P<pk>\d+)$', views.EducationDetail.as_view()),
    # ---------------------------------------------------------------------------------
    re_path(r'^schoolcycle/$', views.CatSchoolCycleList.as_view()),
    re_path(r'^schoolcycle/(?P<pk>\d+)$', views.CatSchoolCycleDetail.as_view()),
    # ---------------------------------------------------------------------------------
    re_path(r'^schoolperiod/$', views.CatSchoolPeriodList.as_view()),
    re_path(r'^schoolperiod/(?P<pk>\d+)$', views.CatSchoolPeriodDetail.as_view()),
    # ---------------------------------------------------------------------------------
    re_path(r'^educationsystem/$', views.CatEducationSystemList.as_view()),
    re_path(r'^educationsystem/(?P<pk>\d+)$', views.CatEducationSystemDetail.as_view()),
]
