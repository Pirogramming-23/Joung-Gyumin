from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.create_post, name='create_post'),
    #path('like/<int:post_id>/', views.toggle_like, name='toggle_like'),
    #path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('comment/delete-ajax/<int:comment_id>/', views.delete_comment_ajax, name='delete_comment_ajax'),
    path('like-ajax/<int:post_id>/', views.toggle_like_ajax, name='toggle_like_ajax'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    
    path('add_comment_ajax/<int:post_id>/', views.add_comment_ajax, name='add_comment_ajax'),
    #path('accounts/logout/', LogoutViewAllowGet.as_view(next_page='post_list'), name='logout'),
]

