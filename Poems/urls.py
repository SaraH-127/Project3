from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('process_message', views.post_mess),
    path('add_comment/<int:id>', views.post_comment),
    path('user_profile/<int:id>', views.profile),
    path('like/<int:id>', views.add_like),
    path('delete/<int:id>', views.delete_comment),
    path('destroy/<int:id>', views.delete_post),
    path('edit/<int:id>', views.edit),
    path('writings/', views.story),
    path('writings/new', views.new),
    path('writings/create', views.create),
    path('writings/<int:writing_id>/editor', views.editor),
    path('writings/<int:writing_id>/update', views.update),
    path('writings/<int:writing_id>', views.writing),
    path('writings/<int:writing_id>/to_delete', views.to_delete),
    path('about', views.about),
    path('cart', views.cart),

]