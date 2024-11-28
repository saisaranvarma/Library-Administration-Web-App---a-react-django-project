from django.urls import path
from . views import *
from . import views

urlpatterns = [
    path('create/',userCreateView.as_view(),name="createuser"),
    path('detail/<int:pk>/',userDetailView.as_view(),name="userdetail"),
    path('update/<int:pk>/',userUpdateView.as_view(),name="updateuser"),
    path('delete/<int:pk>/',userDeleteView.as_view(),name="deleteuser"),


    path('createadmin/',adminCreateView.as_view(),name='create-admin'),
    path('admindetails/<int:pk>/',adminDetails.as_view(),name='admin-details'),
    path('adminupdate/<int:pk>/',adminUpdateView.as_view(),name='admin-update'),
    path('admindelete/<int:pk>/',adminDelete.as_view(),name='admin-delete'),


    path('createbook/',bookcreateview.as_view(),name='createbook'),
    path('bookdetails/<int:pk>/',bookdetailview.as_view(),name='bookdetail'),
    path('bookupdate/<int:pk>/',bookupdateview.as_view(),name='bookupdate'),
    path('bookdelete/<int:pk>/',bookdeleteview.as_view(),name='bookdelete'),


]