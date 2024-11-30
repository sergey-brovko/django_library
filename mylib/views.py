from django.shortcuts import render, redirect

from mylib.form import BookModelForm
from mylib.models import Book


def add_book_form(request):
    if request.method == 'POST':
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookModelForm()

    return render(request, 'mylib/add_book.html', {'form': form, 'title': 'Добавить книгу'})


def edit_book_form(request, id):
    if request.method == 'POST':
        form = BookModelForm(request.POST)
        if form.is_valid():
            book_to_edit = Book.objects.get(pk=int(id))
            book_to_edit.title = form.cleaned_data['title']
            book_to_edit.author = form.cleaned_data['author']
            book_to_edit.price = form.cleaned_data['price']
            book_to_edit.save()
            return redirect('/')
    else:
        form = BookModelForm()

    return render(request, 'mylib/add_book.html', {'form': form, 'title': 'Изменить книгу'})

def delete_book(request, id):
    book_to_delete = Book.objects.get(pk=int(id))
    book_to_delete.delete()
    return redirect('/')

def home(request):
    books = Book.objects.all()
    return render(request, 'mylib/home.html', {'books': books})