from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('dologin/', views.dologin, name='dologin'),
    path('logout/', views.logout, name='logout'),
    path('addVenda/', views.addVenda, name='addVenda'),
    path('historico/', views.historico, name='historico'),
    path('deleteVenda/<id>', views.deleteVenda, name='deleteVenda'),
    path('editMeta/', views.editMeta, name='editMeta'),
]