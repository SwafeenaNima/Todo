from django.urls import path, include

from todoapp import views
app_name='todoapp'
urlpatterns = [
    path('', views.add,name='add'),
    #path('details', views.details,name='details'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    #path('cbvhom/',views.TaskListview1.as_view(),name='cbvhom'),
    #path('cbvdel/<int:pk>/', views.TaskDeleteview1.as_view(), name='cbvdel'),

]
