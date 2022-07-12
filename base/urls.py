from django.urls import path 
from .views import TaskCreate, TaskList  , TaskDetail, TaskReorder , TaskUpdate , DeleteView , CostomLoginView , RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/' , CostomLoginView.as_view() , name='login' ),
    path('logout/' , LogoutView.as_view(next_page='login'), name='logout' ),
    path('register/' , RegisterPage.as_view(), name='register'),


    path('' , TaskList.as_view() , name='tasks'),
    path('task/<int:pk>/' , TaskDetail.as_view() , name="task"),
    path('task-create/' , TaskCreate.as_view() , name="task-create"),
    path('task-update/<int:pk>/' , TaskUpdate.as_view() , name="task-update"),
    path('task-delete/<int:pk>/' , DeleteView.as_view() , name="task-delete"),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
]