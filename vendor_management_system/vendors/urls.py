from django.urls import path
from .views import VendorListCreateAPIView, VendorRetrieveUpdateDestroyAPIView, \
                   PurchaseOrderListCreateAPIView, PurchaseOrderRetrieveUpdateDestroyAPIView, VendorPerformanceAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/vendors/', VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:vendor_id>/', VendorRetrieveUpdateDestroyAPIView.as_view(),
         name='vendor-retrieve-update-destroy'),
    path('api/purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:po_id>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(),
         name='purchase-order-retrieve-update-destroy'),
    path('api/vendors/<int:vendor_id>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]