from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import format_html
# Create your models here.

class Post2(models.Model) :
    title=models.CharField(max_length=50 , default='no title')
    text=models.TextField()
    author=models.ForeignKey(User , on_delete=models.CASCADE)
    published=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    STATUS_CHOICES=(('draft','Draft') , ('published' , 'Published'))
    status=models.CharField(max_length=15 , default='draft' , choices=STATUS_CHOICES)
    photo=models.ImageField(upload_to='media/',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    def photo_tag(self):
        if self.photo:
            return format_html("<img src='{}' width=100 height=100 >".format(self.photo.url))