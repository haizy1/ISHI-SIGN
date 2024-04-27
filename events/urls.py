from django.urls import path, include
from . import views
from cert import views
urlpatterns = [
     path('',views.home, name="home"),
     path('cert/',views.cert_view, name="cert"),
      path('signature/',views.signature_view, name="signature"),
]
