from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Sorry, but your basket is empty")
        return redirect(reverse('products'))
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JvhPRAVVq1DzNNr51AiOy6T6HFOcR6qVYU3UWpGgDQnCsaSKnZ7UGuC4kgHLq4eUjVK9zqRb2qJDeboC1TTfBmg007qiDPC8c',
        'client_secret': 'sk_test_51JvhPRAVVq1DzNNrZRoWnUdX5NBY8HKwPqTrkYUXjzk6948IbX4q6AHTMdi2jh1UgMaKGIcPIe99bh2X0pe5a33w008Ts0rAsg',
    }

    return render(request, template, context)
