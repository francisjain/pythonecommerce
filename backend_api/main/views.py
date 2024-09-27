
from rest_framework import generics,permissions,pagination,viewsets
from . import serializer,models

# Create your views here.

class VendorList(generics.ListCreateAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializer.VendorSerilaizer
    # permission_classes=[permissions.IsAuthenticated]

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializer.VendorDetailSerilaizer
    # permission_classes=[permissions.IsAuthenticated]

class ProductList(generics.ListCreateAPIView):
    queryset=models.Product.objects.all()
    serializer_class=serializer.ProductListSerilaizer
    pagination_class=pagination.PageNumberPagination

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Product.objects.all()
    serializer_class=serializer.ProductDetailSerilaizer


#Customers
class CustomerList(generics.ListCreateAPIView):
    queryset=models.Customer.objects.all()
    serializer_class=serializer.CustomerSerilaizer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Customer.objects.all()
    serializer_class=serializer.CustomerDetailSerilaizer


#Order
class OrderList(generics.ListCreateAPIView):
    queryset=models.Order.objects.all()
    serializer_class=serializer.OrderSerilaizer
    # permission_classes=[permissions.IsAuthenticated]

class OrderDetail(generics.ListAPIView):
    # queryset=models.OrderItems.objects.all()
    serializer_class=serializer.OrderDetailSerilaizer

    def get_queryset(self):
        order_id=self.kwargs['pk']
        order=models.Order.objects.get(id=order_id)
        order_item=models.OrderItems.objects.filter(order=order)
        return order_item


class CustomerAddressViewSet(viewsets.ModelViewSet):
    serializer_class=serializer.CustomerAddressSerilaizer
    queryset=models.CustomerAddress.objects.all()


# class ProductRatingViewSet(viewsets.ModelViewSet):
#     serializer_class=serializer.ProductRatingSerilaizer
#     queryset=models.ProductRating.objects.all()

