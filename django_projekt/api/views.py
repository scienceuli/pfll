from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from api.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserListView(ListView):
    model = User
    template_name = "user_table.html"

class UserDetailView(DetailView):
    model = User
    template_name = "user_detail.html"
