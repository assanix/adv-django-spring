from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserViewSet, ProjectViewSet, CategoryViewSet, PriorityViewSet, TaskViewSet, RegisterUserView

urlpatterns = [
    path('users/', UserViewSet.as_view(), name='user-view'),
    path('projects/', ProjectViewSet.as_view(), name='project-view'),
    path('categories/', CategoryViewSet.as_view(), name='category-view'),
    path('priorities/', PriorityViewSet.as_view(), name='priority-view'),
    path('tasks/', TaskViewSet.as_view(), name='task-view'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),

    path('auth-token/', obtain_auth_token, name='auth-token'),
]

