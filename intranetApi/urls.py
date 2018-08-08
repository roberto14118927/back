from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
    re_path(r'^api/v1/login/', include('login.urls')), 
    re_path(r'^api/v1/settings/', include('globalsettings.urls')), 
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^api/v1/registration/', include('rest_auth.registration.urls')),
    re_path(r'^api/v1/leads/', include('leads.urls')),
    re_path(r'^api/v1/school/', include('school.urls')),
    re_path(r'^api/v1/drive/', include('drive.urls')),
]
