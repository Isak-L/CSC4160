from django.urls import path
from . import views

urlpatterns = [
    path('<str:doctorID>/<str:patientID>', views.result, name = 'result'),
]