from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here:

# class PostManager(models.Manager):
#     def year(self, y):
#         return self.filter(publish__year=y)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('published', 'Published'),
        ('draft', 'Draft')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    titles = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('blog:post-detail', args=[self.slug, self.id])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.titles


class Account(models.Model):
    SEX_CHOICES = (
        ('مرد', 'مرد'),
        ('زن', 'زن')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    # password = models.CharField(max_length=140)
    sex = models.CharField(max_length=5, choices=SEX_CHOICES, default='مرد')
    phone = models.CharField(max_length=11, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    age = models.PositiveIntegerField(default='0', blank=True, null=True)

    # birthday = models.DateTimeField()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'کامنت توسط {self.name} روی پست {self.post}'
