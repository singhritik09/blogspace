from django.db import models
from django.utils import timezone
from matplotlib.pyplot import text
#from django.core.urlresolvers import reverse
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    create_date=models.DateTimeField(default=timezone.now())
    published_date=models.DateTimeField(blank=True,null=True)
    
    def publish(self):
        self.published_date=timezone.now() 
        self.save()
        
    def approve_comments(self):
        return self.comments.filter(approved_comments=True)
    
    def get_absolute_url(self):
        return reverse("post_details",kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    post=models.ForeignKey('blog.Post',related_name='comments', on_delete=models.CASCADE,)
    author=models.CharField(max_length=200)
    text=models.CharField(max_length=200)
    create_data=models.DateTimeField(default=timezone.now())
    
    approved_comments=models.BooleanField(default=True)
    
    def approve(self):
        self.approved_comments=True
        self.save()
        
    def __str__(self):
        return self.text
    
    #absolute urlsyntax and code is defined by django by default
    def get_absolute_url(self):
        return reverse('post_details')
