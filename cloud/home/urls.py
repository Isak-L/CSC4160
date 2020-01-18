from django.urls import path

from . import views
#from .views import SearchResultsView

urlpatterns = [
    path('<str:doctorID>', views.result_list, name = 'result_list'),
    path('result/', views.view_detail, name = 'view_detail'),
]