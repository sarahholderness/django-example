from django.contrib import admin

# import your model
from collectionapp.models import Post, Article

# set up automated slug creation
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('name', 'description', 'user', 'slug',)
    prepopulated_fields = {'slug': ('name',)}

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('headline', 'author', 'picture', 'slug',)
    prepopulated_fields = {'slug': ('headline',)}

# and register it
admin.site.register(Post, PostAdmin)
admin.site.register(Article, ArticleAdmin)