
from django.urls import path
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('address',views.CustomerAddressViewSet)
# router.register('productrating',views.ProductRatingViewSet)

urlpatterns = [
    path('vendor/', views.VendorList.as_view()),
    path('vendor/<int:pk>/', views.VendorDetail.as_view()),

    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),

    #Customers
    path('customer/', views.CustomerList.as_view()),
    path('customer/<int:pk>/', views.CustomerDetail.as_view()),

    #Order
    path('order/', views.OrderList.as_view()),
    path('order/<int:pk>/', views.OrderDetail.as_view()),
]


urlpatterns += router.urls