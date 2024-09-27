from rest_framework import serializers
from . import models

class VendorSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=models.Vendor
        fields=['id','user','address']
    
    def __init__(self, *args, **kwargs):
        super(VendorSerilaizer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1

class VendorDetailSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=models.Vendor
        fields=['id','user','address']
    
    def __init__(self, *args, **kwargs):
        super(VendorDetailSerilaizer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1

class ProductListSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=models.Product
        fields=['id','category','vendor','title','detail','price']
        # depth=1

class ProductDetailSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=models.Product
        fields=['id','category','vendor','title','detail','price']
        # depth=1



class CustomerSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=models.Customer
        fields=['id','user','mobile']
    
    def __init__(self, *args, **kwargs):
        super(CustomerSerilaizer,self).__init__(*args, **kwargs)
        # self.Meta.depth = 1

class CustomerDetailSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=models.Customer
        fields=['id','user','mobile']
    
    def __init__(self, *args, **kwargs):
        super(CustomerDetailSerilaizer,self).__init__(*args, **kwargs)
        # self.Meta.depth = 1

class OrderSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=models.Order
        fields=['id','customer','order_time']
    
    def __init__(self, *args, **kwargs):
        super(OrderSerilaizer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1

class OrderDetailSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=models.OrderItems
        fields=['id','order','product']
    
    def __init__(self, *args, **kwargs):
        super(OrderDetailSerilaizer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class CustomerAddressSerilaizer(serializers.ModelSerializer):
    class  Meta:
        model=models.CustomerAddress
        fields=['id','customer','address','default_address']
        
    def __init__(self, *args,**kwargs):
        super(CustomerAddressSerilaizer,self).__init__(*args, **kwargs)
        self.Meta.depth=1

# class ProductRatingSerilaizer(serializers.ModelSerializer):
#     class  Meta:
#         model=models.ProductRating
#         fields=['id','customer','product','rating','reviews', 'add_time']
        
#     def __init__(self, *args,**kwargs):
#         super(ProductRatingSerilaizer,self).__init__(*args, **kwargs)
#         self.Meta.depth=1

