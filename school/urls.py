from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from school import views
from . import views
urlpatterns = [
    re_path(r'^grade/$', views.schoolGradeList.as_view()),
    re_path(r'^grade/(?P<id>\d+)$', views.schoolGradeDetail.as_view()),
    #paths school
    re_path(r'^weekday/$', views.schoolWeekDayList.as_view()),
    re_path(r'^weekday/(?P<id>\d+)$', views.schoolWeekDayDetail.as_view()),
    #paths 
    re_path(r'^originlevel/$', views.schoolOriginLevelList.as_view()),
    re_path(r'^originlevel/(?P<id>\d+)$', views.schoolOriginLevelDetail.as_view()),
    #paths schoolof Origins
    re_path(r'^origin/$', views.schoolOfOriginList.as_view()),
    re_path(r'^origin/(?P<id>\d+)$', views.schoolOfOriginDetail.as_view()),
    #paths school Materias
    re_path(r'^materia/$', views.schoolMateriaList.as_view()),
    re_path(r'^materia/(?P<id>\d+)$', views.schoolMateriaDetail.as_view()),
    #paths school Groups
    re_path(r'^group/$', views.schoolGroupList.as_view()),
    re_path(r'^group/(?P<id>\d+)$', views.schoolGroupDetail.as_view()),
    #schoolGroup Materia group student
    re_path(r'^groupmateriastudent/$', views.schoolGroupMateriaStudentList.as_view()),
    re_path(r'^groupmateriastudent/(?P<id>\d+)$', views.schoolGroupMateriaStudentDetail.as_view()),
    #path school student parents
    re_path(r'^studentparent/$', views.studentParentList.as_view()),
    re_path(r'^studentparent/(?P<id>\d+)$', views.studentParentDetail.as_view()),
]