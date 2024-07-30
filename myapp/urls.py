from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:page>', views.post, name='post'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit')
]
