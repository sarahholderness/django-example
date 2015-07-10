from django.contrib.auth.models import User
from django.db import models

# Post is like a profile right now -- a user can only have one
class Post(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, blank=True, null=True)

    def __str__(self):
        return str(self.name) + " " + str(self.user)
# Now we want to add an article, or post, or instagram post or whatever
# Using a Many-to-one relationship, ForeignKey
class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    author = models.ForeignKey(User, blank=True, null=True)
    picture = models.ImageField(upload_to='photos/', default='photos/None/no-img.jpg')

    def __str__(self):              # __unicode__ on Python 2
        return self.headline