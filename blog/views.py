from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import NewBlog
from .forms import BlogForm


def all_blogs(request):
    """ A view displaying reviews for the chosen product """
    # currently all reviews displaying
    blogs = NewBlog.objects.all()

    template = 'blog/view_blogs.html'
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
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            blog.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('view_blogs'))
        else:
            messages.error(request, 'Failed to add product.\
                           Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
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
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog!')
            return redirect(reverse('view_blog'))
        else:
            messages.error(request, 'Failed to update blog.\
                           Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.blog_title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
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
    return redirect(reverse('blogs'))
