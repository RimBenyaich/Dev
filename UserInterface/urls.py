from django.urls import path
from UserInterface import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.UI, name='UI'),
    path('checking/', views.checking, name='checking'),
    path('clean/', views.clean, name='clean'),
    path('cleancontinued/', views.cleancontinued, name='cleancontinued'),
    path('correlation/', views.correlation, name="correlation"),
    path('modelling/', views.modelling, name="modelling")
    # path('final/', views.final, name = "final"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
