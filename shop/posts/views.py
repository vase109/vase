from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Post2
from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
# Create your views here.

# def post_list(request):
#     post=Post2.objects.all()
#     context={'post':post}
#     return render (request , "posts/index.html",context)

class Post_list(ListView):
    model = Post2 
    template_name="posts/index.html"
    context_object_name="post"
    
# def post_detail(request,detail_id):
#     detail=Post2.objects.get(id=detail_id)
#     context={'detail':detail}
#     return render (request , "posts/detail.html",context)

class Post_detail(DetailView):
    model = Post2 
    template_name="posts/detail.html"
    context_object_name="detail"
    
class PostCreateView(CreateView):
    model=Post2
    template_name="posts/form.html"
    fields=['title' , 'text' ,'author' ]

class PostEditView(UpdateView) :
    model=Post2
    template_name="posts/edit.html"
    fields=['title' , 'text'  ]

class PostDeleteView(DeleteView):
    model=Post2
    template_name="posts/delete.html"
    success_url= reverse_lazy('create_form')
    