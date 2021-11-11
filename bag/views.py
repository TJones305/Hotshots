from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """A view to return the bag items page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add quantity of a product to shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.info(request,
                              f'Updated {product.name} {size.upper()} Qty to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request,
                                 f'{product.name} {size.upper()} added to basket')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                             f'{product.name} {size.upper()} added to basket')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.info(request,
                          f'Updated {product.name} Qty to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request,
                             f'{product.name} added to basket')

    request.session['bag'] = bag
    return redirect(redirect_url)


def modify_bag(request, item_id):
    """ Modify amount of an item & display price """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.info(request,
                          f'Updated {product.name} {size.upper()} Qty to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.warning(request,
                                 f'{product.name} {size.upper()} removed from basket')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.info(request,
                          f'Updated {product.name} Qty to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.warning(request,
                             f'{product.name} Removed from basket')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_bag_item(request, item_id):
    """ Remove item from basket """

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.warning(request,
                                 f'{product.name} {size.upper()} removed from basket')
        else:
            bag.pop(item_id)
            messages.warning(request,
                             f'{product.name} Removed from basket')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error occured: {e}')
        return HttpResponse(status=500)
