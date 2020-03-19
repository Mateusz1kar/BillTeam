
from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('',views.index,name='index'),
    path('PersonList/', views.PersonList.as_view(), name='personList'),
    path('AddPerson/', views.addPerson, name='addPerson'),
    path('DetailPerson/<int:pk>/', views.DetailPerson.as_view(), name='detailPerson'),
    # ex: /polls/5/results/
   # path('detailProject/<int:idProject>/', views.detailProject, name='detailProject'),
    # ex: /polls/5/vote/
   # path('detailNotification/<int:idNotification>/', views.detailNotification, name='detailNotification'),
    path('PersonFormExecute/', views.personFormExecute, name='personFormExecute'),
    path('PersonFormDeleteExecute/', views.personFormDeleteExecute, name='personDelee'),
    path('AddPersonFormExecute/', views.addPersonFormExecute, name='personAdd'),

    path('ProjectList/', views.ProjectList.as_view(), name='projectList'),
]
