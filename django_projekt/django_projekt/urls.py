from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views
from api.views import UserListView, UserDetailView


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Use automatic URL routing
# Can also include login URLs for the browsable API

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('all-users/', UserListView.as_view(), name='all-users'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-details')
]