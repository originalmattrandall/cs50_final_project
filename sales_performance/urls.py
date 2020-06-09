from django.urls import path, reverse
from .views import SaleCreateView
from . import views

urlpatterns = [
    path('', views.home, name='sales-performance-home'),
    path('data-management/', views.data_management, name='sales-performance-data-management'),
    path('data-visualization/', views.data_visualization, name='sales-performance-data-visualization'),
    path('data-visualization/sale-api/', views.chart_data, name='sale-api'),
    # CRUD views
    path('sale/new/', SaleCreateView.as_view(), name='sale-create')
]
