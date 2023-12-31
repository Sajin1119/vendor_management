# vendor_app/urls.py
from django.urls import path
from .views import (
    VendorListCreateView,
    VendorRetrieveUpdateDeleteView,
    PurchaseOrderListCreateView,
    PurchaseOrderRetrieveUpdateDeleteView,
    VendorPerformanceRetrieveView,
)

urlpatterns = [
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', VendorRetrieveUpdateDeleteView.as_view(), name='vendor-retrieve-update-delete'),
    path('purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDeleteView.as_view(), name='purchase-order-retrieve-update-delete'),
    path('vendors/<int:pk>/performance/', VendorPerformanceRetrieveView.as_view(), name='vendor-performance-retrieve'),
]
