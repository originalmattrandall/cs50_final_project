from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sales-performance-home'),
    path('data-management/', views.data_management, name='sales-performance-data-management'),
    path('data-visualization/', views.data_visualization, name='sales-performance-data-visualization'),
    path('chart-data/', views.chart_data, name='chart-data')
]