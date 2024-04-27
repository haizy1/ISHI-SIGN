from django.urls import path
from . import views


urlpatterns = [
    path('events/',views.home, name="home"),
    path('cert/',views.cert_view, name="cert"),
    path('signature/',views.signature_view, name="signature"),
    path('verification/',views.verification_view, name="verification"),
    path('paiement/',views.paiement_view, name="paiement"),
]