from django.urls import path
from . import views
from . views import create_post, view_post, all_post, update_post
urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/', create_post, name="create_posts"),
    path('all_post/', all_post, name="all_post"),
    path('view_post/<int:id>', view_post, name="view_post"),
    path('update_post/<int:id>', update_post, name="update_post")
]