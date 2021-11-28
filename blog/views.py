from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import NewBlog
from .forms import BlogForm


def all_blogs(request):
    """ A view displaying reviews for the chosen product """
    # currently all reviews displaying
    blogs = NewBlog.objects.all()

    template = 'blog/view_blog.html'
    context = {
        'blogs': blogs,
    }

    return render(request, template, context)


@login_required
def add_blog(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Whoops! did you get lost?,\
                       You do not have permissons access this area!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog = blog_form.save()
            blog.save()
            messages.success(request, 'Successfully added blog!')
            return redirect(reverse('view_blogs'))
        else:
            messages.error(request, 'Failed to add blog.\
                           Please ensure the form is valid.')
    else:
        blog_form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'blog_form': blog_form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Whoops! did you get lost?,\
                       You do not have permissons access this area!')
        return redirect(reverse('home'))

    blog = get_object_or_404(NewBlog, pk=blog_id)
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES, instance=blog)
        if blog_form.is_valid():
            blog_form.save()
            messages.success(request, 'Successfully updated blog!')
            return redirect(reverse('view_blogs'))
        else:
            messages.error(request, 'Failed to update blog.\
                           Please ensure the form is valid.')
    else:
        blog_form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.blog_title}')

    template = 'blog/edit_blog.html'
    context = {
        'blog_form': blog_form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Whoops! did you get lost?,\
                       You do not have permissons access this area!')
        return redirect(reverse('home'))

    blog = get_object_or_404(NewBlog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog deleted!')
    return redirect(reverse('view_blogs'))
