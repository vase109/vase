from django.urls import path
from . import views

urlpatterns = [
    path('', views.Post_list.as_view() , name='post_list'),
    path('<int:pk>/' ,views.Post_detail.as_view() , name="post_detail"),
    path('form/' ,views.PostCreateView.as_view() , name="create_form"),
    path('<int:pk>/edit/' ,views.PostEditView.as_view() , name="edit_form"),
    path('<int:pk>/delete/' ,views.PostDeleteView.as_view() , name="delete_form"),
    
]