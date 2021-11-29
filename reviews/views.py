from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from profiles.models import UserProfile
from .models import UserReview
from .forms import ReviewForm


def product_reviews(request):
    """ A view displaying reviews for the chosen product """
    # currently all reviews displaying
    reviews = UserReview.objects.all()

    template = 'reviews/product_review.html'
    context = {
        'reviews': reviews,
    }

    return render(request, template, context)


@login_required
def add_review(request, product_id):
    """Enables registered user to add a review"""
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            r = review_form.save(commit=False)
            r.product = product
            r.user = UserProfile.objects.get(user=request.user)
            r.save()

            messages.success(request,
                             'Your feedback is important, Thanks!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Oh no! There was an error.\
                           Please check the form is valid and resubmit')
    else:
        review_form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'review_form': review_form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """Enables register user to edit a review"""
    review = get_object_or_404(UserReview,
                               pk=review_id)
    
    print(review.product_id)

    if not request.user.is_superuser or request.user == review.user:
        messages.error(request, 'Whoops! did you get lost?,\
                       You do not have permissons access this area!')
        return redirect(reverse('home'))

    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            r = review_form.save(commit=False)
            r.product = review.product
            r.save()
            messages.success(request,
                             'Review edited!')

            return redirect(reverse('products'))
        else:
            messages.error(request, 'Oh no! There was an error.\
                            Please check the form is valid and resubmit')
    else:
        review_form = ReviewForm(instance=review)
        messages.info(request, 'You are editing this review!')

    template = 'reviews/edit_review.html'
    context = {
        'review_form': review_form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """Enables register user to delete a review"""
    if not request.user.is_superuser:
        messages.error(request, 'Whoops! did you get lost?,\
                       You do not have permissons access this area!')
        return redirect(reverse('home'))

    review = get_object_or_404(UserReview,  pk=review_id)
    review.delete()
    messages.success(request, 'Review Deleted!')

    return redirect(reverse('products'))
