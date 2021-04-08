from django.urls import path
from UserInterface import views

urlpatterns = [
    path('', views.UI, name='UI'),
    path('download/', views.download, name='download'),
    path('check/', views.check, name = 'check'),
    #path('clean/', views.clean, name = 'clean'),
]