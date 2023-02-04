from django.urls import path
from base import views

urlpatterns = [
    path('all_post', views.get_posts, name="posts"),
    path('post/<str:pk>', views.get_post, name="post"),
    path('category/<str:pk>', views.get_category, name="category"),
    path('create_post/', views.CreatePost.as_view(), name="create-post"),
    path('funcion_post_create/', views.postCreate, name="function-post-create")
]
