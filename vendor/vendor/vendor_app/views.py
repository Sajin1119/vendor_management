from django.shortcuts import render
from rest_framework import generics
from .models import Vendor, PurchaseOrder, VendorPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, VendorPerformanceSerializer


# Create your views here.


class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class VendorPerformanceRetrieveView(generics.RetrieveAPIView):
    queryset = VendorPerformance.objects.all()
    serializer_class = VendorPerformanceSerializer
