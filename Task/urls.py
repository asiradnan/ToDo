from django.urls import path
from . import views
app_name ="Task"
urlpatterns=[
    path("add/",views.addTask,name="addtask"),
    path('',views.home,name="home"),
    path('delete/<int:id>',views.delete,name="delete")
]