from django.urls import path

from mylib import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_book', views.add_book_form, name='add_book'),
    path('delete/<str:id>', views.delete_book, name='delete'),
    path('edit/<str:id>', views.edit_book_form, name='edit'),

]