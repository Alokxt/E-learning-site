from django.shortcuts import render,redirect
from .models import shopsy
from .forms import searchForm
from .models import cartitem
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import paypalrestsdk
from django.conf import settings
from django.http import JsonResponse
from .paypal_utils import create_payment, execute_payment
paypalrestsdk.configure({
    "mode": "sandbox",  # Use "live" for production
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})
    

def initiate_payment(request):
    total_amount =  total_bill(request) 
    return_url = request.build_absolute_uri('/payment-success/')
    cancel_url = request.build_absolute_uri('/payment-cancelled/')
    print("Return URL:", return_url)
    print("Cancel URL:", cancel_url)
    
    payment = create_payment(total_amount,  currency="USD",return_url=return_url, cancel_url=cancel_url)
    
    if payment:
        # Redirect to PayPal for payment approval
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)
    return JsonResponse({"error": "Payment creation failed"}, status=400)

def payment_success(request):
    payment_id = request.GET.get("paymentId")
    payer_id = request.GET.get("PayerID")
    
    payment = execute_payment(payment_id, payer_id)
    if payment:
        cartitem.objects.filter(user=request.user).delete()
    
        return render(request, "payment_success.html", {"payment": payment})
    return JsonResponse({"error": "Payment execution failed"}, status=400)

def payment_cancelled(request):
    return render(request, "payment_cancelled.html")



def productpage(request):
    return render(request,'shop2.html') 
@login_required


def total_bill(request):
    from decimal import Decimal
    cart_items = cartitem.objects.filter(user = request.user)
    total =Decimal(0)
    if(cart_items):
        for o in cart_items:
             total += Decimal(o.quantity) * Decimal(o.product.prize)
    return total


def cart_view(request):
    cart_items = cartitem.objects.filter(user = request.user)
    total =0
    if(cart_items):
        for o in cart_items:
            total = total + o.product.prize
    
    context = {'cart_items':cart_items,'bill':total}
    
    return render(request,'shopcart.html',context)

@login_required
def add_To_cart(request,item_id):
    item = get_object_or_404(shopsy,id=item_id)
    cart_item,created = cartitem.objects.get_or_create(user=request.user,product = item)

    if not created:
        cart_item.quantity +=1 
        cart_item.save()
    return redirect('wish-list')
    



def mainpage(request):
    if(request.method == "POST"):
        form = searchForm(request.POST)
        if(form.is_valid()):
            item = form.cleaned_data.get('item_name')
            all = shopsy.objects.all()
            field = shopsy.objects.filter(item_name = item)
            print(item)
            print(field)
            context = {'form':form,'list':field,'objs':all}
            return render(request,'shop2.html',context)
            
            #for items in all:
             #   if items.item_field == field:
              #      l.append(items.item_name)
               #     context = {'form':form,'list':l}
                    
                

    else:
        form = searchForm()
    context = {'form':form}


    return render(request,'shop.html',context)


def search_items(request):
    query = request.GET.get('q','').strip()
    print(query)
    items =[]
    
    if(query):
        items = shopsy.objects.filter(item_name__icontains=query)
    l =[]
    for p in items:
        d= {
            'name':p.item_name,
            'id':p.id,
        }
        l.append(d)

    print(items)
    return JsonResponse({'results':l})

def productview(request,item_id):
    item = shopsy.objects.get(id = item_id)
    return render(request,'productview.html',{'item':item})
