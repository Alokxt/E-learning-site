from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('shop/',views.mainpage,name ="store"),
    path('products/',views.productpage,name ="products"),
    path('cart/',views.cart_view,name ="wish-list"),
    path('item-add/<int:item_id>/',views.add_To_cart,name = "add-item"),
    path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
    path('search-items/api/',views.search_items,name="search_items"),
    path('productview/<int:item_id>/',views.productview,name="product-view"),

]
