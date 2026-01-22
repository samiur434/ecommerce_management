from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponseBadRequest

from django.contrib import messages
from math import ceil

# Create your views here.
def Home(request):
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prods=Product.objects.filter(category=cat)
        n=len(prods)
        nslides=n//4+ceil((n/4)-(n//4))
        allprods.append([prods,range(1,nslides),nslides])
    params={'allprods':allprods}
    return render(request, 'index.html',params)


def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/login')

    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        Order = Orders(items_json=items_json,name=name,amount=amount, email=email, address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,phone=phone)
        print(amount)
        Order.save()
        update = OrderUpdate(order_id=Order.order_id,update_desc="the order has been placed")
        update.save()
        thank = True
# # PAYMENT INTEGRATION

        # id = Order.order_id
        # oid=str(id)+"ShopyCart"
        # param_dict = {

        #     'MID':keys.MID,
        #     'ORDER_ID': oid,
        #     'TXN_AMOUNT': str(amount),
        #     'CUST_ID': email,
        #     'INDUSTRY_TYPE_ID': 'Retail',
        #     'WEBSITE': 'WEBSTAGING',
        #     'CHANNEL_ID': 'WEB',
        #     'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

        # }
        # param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        # return render(request, 'paytm.html', {'param_dict': param_dict})

    return render(request, 'checkout.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        phonenumber = request.POST.get('phonenumber')
        
        # Print out the received form data for debugging
        print("Received form data:", request.POST)

        # Check if any of the required fields are missing
        if not all([name, email, desc, phonenumber]):
            return HttpResponseBadRequest("Missing required fields")

        # Create a Contact object and save it
        contact = Contact(name=name, email=email, desc=desc, phonenumber=phonenumber)
        contact.save()
        
        return render(request, 'contact.html')

        
    return render(request, 'contact.html')

        


    
