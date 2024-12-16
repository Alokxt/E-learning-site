
import paypalrestsdk
from django.contrib.auth.decorators import login_required
import paypalrestsdk
from django.conf import settings




paypalrestsdk.configure({
    "mode": "sandbox",  # Use "live" for production
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})

def create_payment(total_amount, currency="USD", return_url=None, cancel_url=None):
    total = total_amount
    payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {"payment_method": "paypal"},
            "redirect_urls": {
                "return_url": return_url,
                "cancel_url": cancel_url,
            },
            "transactions": [{
                "amount": {"total": f"{total:.2f}", "currency": currency},
                "description": "E-commerce transaction",
            }]
        })

    if payment.create():
        return payment
    else:
        print(payment.error)
        return None
    

def execute_payment(payment_id, payer_id):
    payment = paypalrestsdk.Payment.find(payment_id)
    if payment.execute({"payer_id": payer_id}):
        return payment
    else:
        print(payment.error)
        return None
    