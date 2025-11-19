from django.urls import path
from . import views


urlpatterns = [

    path('tasks/list/', views.TasksListView.as_view(), name='task_list'),
    path('tasks/create/', views.TasksCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/detail/', views.TasksDetailView.as_view(), name='task_detail'),
    path('tasks/<int:pk>/update/', views.TasksUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', views.TasksDeleteView.as_view(), name='task_delete'),
    path('tasks/<int:pk>/update-status/', views.update_status, name='update_status'),
    path('historic/list/', views.HistoricListView.as_view(), name='historic_list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),

]
