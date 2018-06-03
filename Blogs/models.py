from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(blank=True, null=True)

    def set_author(self):
        slef.author = user.username

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comments=True)

    def unapproved_comments(self):
        return self.comments.filter(approved_comments=False)

    def get_absolute_url(self):
        return reverse('Blogs:post_list')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Blogs.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comments = models.BooleanField(default=False)

    def approve(self):
        self.approved_comments = True
        self.save()

    def get_absolute_url(self):
        return reverse('Blogs:post_list')

    def __str__(self):
        return self.text
