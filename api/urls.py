from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
from api import views

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'sets/(?P<pk>[0-9]+)$', views.SetView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
