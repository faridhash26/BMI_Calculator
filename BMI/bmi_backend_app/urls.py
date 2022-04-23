from django.urls import path

from . import views

urlpatterns = [
    path('bmi/', views.BmiView.as_view(), name='new_bmi'),
    path('bmi/history/', views.BmiListView.as_view(), name='all_bmis'),

]
