import json
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Payment

# Create your views here.
def payment_index(request):
    return render(request, 'payment/index.html', {})


def payment_successful(request):
    context = {'payment': payment}
    return render(request, 'payment/success.html', context)


@csrf_exempt
def payment_handler(request):
    if request.method == "POST":
        paystack_data = json.loads(request.body)
        response_data = {}

      

        email = paystack_data['email']
        amount = paystack_data['amount']
        ref_id = paystack_data['ref_id']
        meta_data = paystack_data['meta']
        
        # create a new application object.
        new_payment = Payment(user=user, email=email, amount=amount, ref_id=ref_id, meta_data=meta_data)
        new_payment.save()

        response_data['email'] = new_payment.email
        response_data['amount'] = new_payment.amount
        response_data['ref_id'] = new_payment.ref_id
        response_data['meta_data'] = new_payment.meta_data

        return HttpResponse(
            json.dumps(response_data), content_type="application/json")

    else:
        return HttpResponse(json.dumps({"response": "error"}), content_type="application/json")

