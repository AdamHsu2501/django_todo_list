from django.urls import path
from .views import TaskCreateView, TaskDeleteView, TaskListView, TaskUpdateView, UserLoginView, UserRegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path(route='login/', view=UserLoginView.as_view(), name="login"),
    path(route='logout/', view=LogoutView.as_view(next_page='login'), name="logout"),
    path(route='register/', view=UserRegisterView.as_view(), name='register'),
    
    path(route='', view=TaskListView.as_view(), name="tasks"),
    path(route='task-create/', view=TaskCreateView.as_view(), name="task-create"),
    path(route='task-update/<int:pk>/', view=TaskUpdateView.as_view(), name="task-update"),
    path(route='task-delete/<int:pk>/', view=TaskDeleteView.as_view(), name="task-delete"),
]
