from django.contrib import admin

# import your model
from collectionapp.models import Post

# set up automated slug creation
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Post, PostAdmin)
