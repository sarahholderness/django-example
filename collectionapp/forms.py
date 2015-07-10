from django.forms import ModelForm
from collectionapp.models import Post, Article

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'description',)

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('headline', 'picture',)
