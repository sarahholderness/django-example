from django.shortcuts import render, redirect
from collectionapp.forms import PostForm, ArticleForm
from collectionapp.models import Post, Article
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils import timezone

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



@login_required
def edit_post(request, slug):
    # grab the object...
    post = Post.objects.get(slug=slug)
    # make sure the logged in user is the owner of the thing
    if post.user != request.user:
        raise Http404

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

@login_required
def create_article(request, slug):
    form_class = ArticleForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but do not save yet
            article = form.save(commit=False)
            article.pub_date = timezone.now()
            article.author = request.user

            # save the object
            article.save()
            # TODO redirect to our newly created thing
            return redirect('post_detail', slug=slug)
    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'articles/create_article.html', {
        'form': form,
    })


def create_post(request):
    form_class = PostForm
    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and apply to # the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but do not save yet
            post = form.save(commit=False)
            # set the additional details
            post.user = request.user
            post.slug = slugify(post.name)
            # save the object
            post.save()
            # redirect to our newly created thing
            return redirect('post_detail', slug=post.slug)
    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'posts/create_post.html', {
        'form': form,
    })

def browse_by_name(request, initial=None):
    if initial:
        posts = Post.objects.filter( name__istartswith=initial).order_by('name')
    else:
        posts = Post.objects.all().order_by('name')
    return render(request, 'search/search.html', {
        'posts': posts,
        'initial': initial,
    })
