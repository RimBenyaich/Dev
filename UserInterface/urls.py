from django.urls import path
from UserInterface import views

urlpatterns = [
    path('', views.UI, name='UI'),
    path('checking/', views.checking, name = 'checking'),
    path('clean/', views.clean, name= 'clean'),
    path('correlation/', views.correlation, name = "correlation"),
    path('modelling/', views.modelling, name = "modelling")
    # path('final/', views.final, name = "final"),
]