from django.db.models import Count, Avg
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer


class VendorListCreateAPIView(APIView):
    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, vendor_id):
        vendor = Vendor.objects.get(pk=vendor_id)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    def put(self, request, vendor_id):
        vendor = Vendor.objects.get(pk=vendor_id)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, vendor_id):
        vendor = Vendor.objects.get(pk=vendor_id)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PurchaseOrderListCreateAPIView(APIView):
    def get(self, request):
        purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseOrderRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, po_id):
        purchase_order = PurchaseOrder.objects.get(pk=po_id)
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)

    def put(self, request, po_id):
        purchase_order = PurchaseOrder.objects.get(pk=po_id)
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, po_id):
        purchase_order = PurchaseOrder.objects.get(pk=po_id)
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VendorPerformanceAPIView(APIView):
    def get(self, request, vendor_id):
        vendor = Vendor.objects.get(pk=vendor_id)

        # Calculate on-time delivery rate
        total_completed_orders = vendor.purchaseorder_set.filter(status='completed').count()
        on_time_deliveries = vendor.purchaseorder_set.filter(status='completed',
                                                             delivery_date__lte=timezone.now()).count()
        on_time_delivery_rate = (on_time_deliveries / total_completed_orders) * 100 if total_completed_orders != 0 \
            else 0

        # Calculate quality rating average
        quality_rating_avg = vendor.purchaseorder_set.filter(status='completed'). \
                                 aggregate(avg_quality=Avg('quality_rating'))['avg_quality'] or 0

        # Calculate average response time
        response_times = vendor.purchaseorder_set.filter(acknowledgment_date__isnull=False).annotate(
            response_time=Count('acknowledgment_date') - F('issue_date')).aggregate(
            avg_response_time=Avg('response_time'))['avg_response_time'] or 0

        # Calculate fulfillment rate
        total_orders = vendor.purchaseorder_set.count()
        successful_orders = vendor.purchaseorder_set.filter(status='completed', quality_rating__isnull=False).count()
        fulfillment_rate = (successful_orders / total_orders) * 100 if total_orders != 0 else 0

        performance_metrics = {
            'on_time_delivery_rate': on_time_delivery_rate,
            'quality_rating_avg': quality_rating_avg,
            'average_response_time': response_times,
            'fulfillment_rate': fulfillment_rate
        }

        return Response(performance_metrics)
