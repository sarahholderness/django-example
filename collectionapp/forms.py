from django.forms import ModelForm
from collectionapp.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'description',)