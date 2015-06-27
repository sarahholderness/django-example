from django.shortcuts import render, redirect
from collectionapp.forms import PostForm
from collectionapp.models import Post


# Create your views here.
def index(request):
    # Define a variable
    posts = Post.objects.all()

    # Pass a variable to the view
    return render(request, 'index.html', {
        'posts': posts,
    })

def post_detail(request, slug):
    # Grab the object
    post = Post.objects.get(slug=slug)
    # Pass to the template
    return render(request, 'posts/post_detail.html', {
        'post': post,
    })

# add below your post_detail view
def edit_post(request, slug):
    # grab the object...
    post = Post.objects.get(slug=slug)
    # set the form we're using...
    form_class = PostForm

    # if we're coming to this view from a submitted form,
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=post)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('post_detail', slug=post.slug)

    # otherwise just create the form
    else:
        form = form_class(instance=post)

    # and render the template
    return render(request, 'posts/edit_post.html', {
        'post': post,
        'form': form,
    })