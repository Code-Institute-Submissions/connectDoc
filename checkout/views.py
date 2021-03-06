from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from medicalPractice.models import Doctor
from django.utils import timezone
import stripe
from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template


stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                doctor = get_object_or_404(Doctor, pk=id)
                total += quantity * doctor.price
                order_line_item = OrderLineItem(
                    order = order,
                    doctor = doctor,
                    quantity = quantity
                    )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount= int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                
                
                # Send Email
                template=get_template('confirmation_email.html')
                context = {
                    'site_name': "Blah Blah dot com",
                }
                content = template.render(context)
                
                subject = 'Get well soon!'
                message = content
                from_email = settings.SYSTEM_EMAIL
                to_email = [request.user.email]
    
                send_mail(subject,message,from_email,to_email,fail_silently=True)

                request.session['cart'] = {}
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        

    return render(request, "checkout.html", {'doctor': doctor, 'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE })