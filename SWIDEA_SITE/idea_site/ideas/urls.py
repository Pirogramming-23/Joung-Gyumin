from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('create/', views.idea_create, name='idea_create'),
    path('idea/<int:idea_id>/', views.idea_detail, name='idea_detail'),
    path('idea/<int:idea_id>/update/', views.idea_update, name='idea_update'),
    path('idea/<int:idea_id>/delete/', views.idea_delete, name='idea_delete'),
    path('tools/', views.devtool_list, name='devtool_list'),
    path('tools/create/', views.devtool_create, name='devtool_create'),
    path('tools/<int:tool_id>/', views.devtool_detail, name='devtool_detail'),
    path('tools/<int:tool_id>/update/', views.devtool_update, name='devtool_update'),
    path('tools/<int:tool_id>/delete/', views.devtool_delete, name='devtool_delete'),
    path('ideas/<int:idea_id>/toggle_star/', views.toggle_star, name='toggle_star'),

]
