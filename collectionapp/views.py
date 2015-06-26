from django.shortcuts import render
from collectionapp.models import Post

# Create your views here.
def index(request):
    # Define a variable
    posts = Post.objects.all()

    # Pass a variable to the view
    return render(request, 'index.html', {
        'posts': posts,
    })