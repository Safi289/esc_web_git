from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('company-info/<int:company_id>/', views.company_info, name="company_info"),
]

