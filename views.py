from django.shortcuts import render, redirect
from .models import List_book
from .forms import BookCreate
# Create your views here.

# Create your views here.


def book_view(request):

    books = List_book.objects.all()

    context = {
        'books': books
    }
    return render(request, 'book/bookhome.html', context)


# def add_book(request):

#     return render(request, 'book/add_book.html')


# def create(request):
#     print(request.POST)
#     name = request.GET['name']
#     title = request.GET['title']
#     price = request.GET['price']
#     author = request.GET['author']
#     isbn = request.GET['isbn']

#     book_details = List_book(title=title, name=name,
#                              price=price, author=author, isbn=isbn)
#     book_details.save()
#     return redirect('booklist/')


def addbook(request):
    form = BookCreate()
    if request.method == 'POST':
        form = BookCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/booklist/')

    context = {'form': form}
    return render(request, 'book/book.html', context)


def updatebooks(request, pk):
    order = List_book.objects.get(id=pk)
    form = BookCreate(instance=order)
    if request.method == 'POST':
        form = BookCreate(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/booklist/')
    context = {'form': form}
    return render(request, 'book/book.html', context)


def deletebooks(request, pk):
	order = List_book.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/booklist/')

	context = {'item':order}
	return render(request, 'book/delete.html', context)