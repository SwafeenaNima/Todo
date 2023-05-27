from django.urls import path, include

from todoclassapp import views
app_name='todoclassapp'
urlpatterns = [

    path('cbvhome/',views.TaskListview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdetail'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='cbvdelete'),
    path('cbvedit/<int:pk>/',views.TaskUpdateview.as_view(),name='cbvedit'),


]
