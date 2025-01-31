from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Vendor Models
class Vendor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField(null=True)
    
    def __str__(self):
        return self.user.username

#Product Category
class ProductCategory(models.Model):
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)

    def __str__(self):
        return self.title   
    
#Product 
class Product(models.Model):
    category=models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True,related_name='category_product')
    vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)
    price=models.FloatField()

    def __str__(self):
        return self.title 

#Customer Models
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.user.username

#Order Models
class Order(models.Model):
     customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer_order')  
     order_time=models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return '%s' % (self.order_time)
     
     
#Order Items Models
class OrderItems(models.Model):
     order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_items')  
     product=models.ForeignKey(Product,on_delete=models.CASCADE)  
    
     def __str__(self):
        return self.product.title


class CustomerAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer_addresses')
    address=models.TextField()
    default_address = models.BooleanField(default=False)

    def __str__(self):
        return self.address

class ProductRating(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='rating_customers')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_ratings')
    rating=models.IntegerField()
    reviews=models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating} - {self.reviews}'
