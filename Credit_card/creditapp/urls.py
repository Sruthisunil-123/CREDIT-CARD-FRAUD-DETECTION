from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.creditcard,name='creditcard'),
    path('register/',views.creditcard),
    path('login/',views.creditlogin,name='creditlogin'),
    path('log/',views.log,name='log'),
    path('dashboard/',views.dashboards,name='dashboard'),
    path('contact/',views.contact,name='contact')
    
]