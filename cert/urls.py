from django.urls import path, include
from . import views
urlpatterns = [
    path('cert/',views.cert_view, name="cert"),
    path('events/',views.home, name="home"),
    path('signature/',views.signature_view, name="signature"),
    path('paiement/',views.paiement_view, name="paiement"),
]