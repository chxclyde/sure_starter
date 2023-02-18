from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addnode/',views.addnode,name='addnode'),
    path('addnode_put/', views.addnode_put,name='addnode_put' ),
    path('add_relation/',views.add_relation,name='add_relation'),
    path('reset_db/',views.reset_db,name ='reset_db' ),
]
