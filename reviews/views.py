from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserReview
from .forms import ReviewForm


def reviews(request):
    """ A view displaying reviews for the chosen product """
    # currently all reviews displaying
    reviews = UserReview.objects.all()

    template = 'reviews/reviews.html'
    context = {
        'reviews': reviews,
    }

    return render(request, template, context)


@login_required
def add_review(request):
    """Enables register user to add a review"""
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your feedback is important, Thanks!')

            return redirect(reverse('reviews',))
        else:
            messages.error(request, 'Oh no! There was an error.\
                           Please check the form is valid and resubmit')
    else:
        form = ReviewForm()

    form = ReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_review(request):
    """Enables register user to edit a review"""
    review = get_object_or_404(UserReview,
                               pk=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Review has been edited')

            return redirect(reverse('reviews',))
        else:
            messages.error(request, 'Oh no! There was an error.\
                            Please check the form is valid and resubmit')
    else:
        form = ReviewForm()

    form = ReviewForm(instance=review)
    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request):
    """Enables register user to delete a review"""
    review = get_object_or_404(UserReview, pk=review_id)
    review.delete()
    messages.success(request, 'The review has been deleted!')

    return redirect(reverse('reviews'))
