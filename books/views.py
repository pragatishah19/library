from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from .forms import BookForm,AuthorForm,GenreForm,UserForm
from .models import Books,Author,User,Genre

from django.core.mail import send_mail
from django.conf import settings

from django.views.generic import(
    DetailView,ListView,UpdateView,DeleteView
)

import datetime
# Create your views here.
def Index_view(request):
    return HttpResponse("<h1>Hello Python</h1>")
def Home_view(request):
    date = datetime.datetime.now()
    str='hello test pragati'
    site = 'www.google.com'
    email = "pragati.shah@gmail.com"
    number = 123456
    context = {
        'email':email,
        'site':site,
        'str': str,
        'num': number,
        'date':date
    }
    return render(request,"Books/home.html",context)
@login_required
def About(request):
    return render(request,"Books/about.html")
def Contact_us(request):
    return render(request,"Books/contact_us.html")
def static_demo_view(request):
    return render(request,"Books/static_demo.html")

def Genre_create_view(request):
    form = GenreForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
    form = GenreForm()
    context = {
        'form' : form
    }
    return render(request,'Books/book_create.html',context)

class BookDetailView(DetailView):
    model=Books
    template_name = "Books/book_detail.html"

    def get_object(self):
        pk=self.kwargs.get('pk')
        return get_object_or_404(Books,pk=pk)

class BookListView(ListView):
    queryset = Books.objects.all()
    template_name = 'Books/book_list_view.html'

class BookCreateView(CreateView):
    template_name = "Books/book_create.html"
    form_class = BookForm

    def get_success_url(self):
        return reverse("books:book_list_view")

class BookUpdateView(UpdateView):
    template_name = "Books/book_update.html"
    form_class = BookForm

    def get_success_url(self):
        return reverse("books:book_list_view")

    def get_object(self):
        pk=self.kwargs.get('pk')
        return get_object_or_404(Books,pk=pk)

class BookDeleteView(DeleteView):
    template_name = "Books/book_delete.html"

    def get_success_url(self):
        return reverse("books:book_list_view")

    def get_object(self):
        pk=self.kwargs.get('pk')
        return get_object_or_404(Books,pk=pk)

def Book_create_view(request):
    form = BookForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
    form=BookForm()
    context = {
        'form' : form
    }
    return render(request,"Books/book_create.html",context)

def Book_update_view(request,pk):
    books=get_object_or_404(Books,pk=pk)
    form = BookForm(request.POST or None,instance=books)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request,'Books/book_update.html',context)

# def Book_delete_view(request,pk):
#     books=get_object_or_404(Books,pk=pk)
#     if request.method =='POST':
#         books.delete()
#         return redirect(reverse('books:book_list_view'))
#     context={
#         'books':books
#     }
#     return render(request,'Books/book_delete.html',context)
def Book_delete_view(request,pk):
    if request.method =='POST':
        books=get_object_or_404(Books,pk=pk)
        books.delete()
        return redirect(reverse('books:book_list1_view'))

# def Book_list_view(request):
#     books = Books.objects.all()
#     context = {
#         'books':books
#     }
#     return render(request,"Books/book_list_view.html",context)

def Book_list_view(request):
    books = Books.objects.all()
    if request.method =='POST':
        form = BookForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
    form=BookForm()
    context = {
        'books_list':books,
        'form':form
    }
    return render(request,"Books/book_list.html",context)

def Book_index_view(request):
    books = Books.objects.all()
    context = {
        'books':books
    }
    return render(request,"Books/book_index.html",context)

def Book_detail_view(request,pk):
    books = get_object_or_404(Books,pk=pk)
    context={
        'books':books
    }
    return render(request,'Books/book_detail.html',context)

class AuthorDetailView(DetailView):
    template_name = 'Books/author_detail.html'
    model = Author

    def get_object(self):
        pk=self.kwargs.get('pk')
        return get_object_or_404(Author,pk=pk)

class AuthorListView(ListView):
    queryset = Author.objects.all()
    template_name = 'Books/author_list_view.html'

def Author_create_view(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('books:author_list_view'))
    form = AuthorForm()
    context = {
        'form' : form
    }
    return render(request,'Books/author_create.html',context)

def Author_update_view(request,pk):
    author =get_object_or_404(Author,pk=pk)
    form = AuthorForm(request.POST or None,instance=author)
    if form.is_valid():
        form.save()
        return redirect(reverse('books:author_list_view'))
    context = {
        'form':form
    }
    return render(request,'Books/author_update.html',context)

def Author_delete_view(request,pk):
    author = get_object_or_404(Author,pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect(reverse('books:author_list_view'))
    context = {
        'author':author
    }
    return render(request,'Books/author_delete.html',context)
    
def Author_list_view(request):
    author = Author.objects.all()
    context = {
        'author':author
    }
    return render(request,"Books/author_list_view.html",context)

def Author_index_view(request):
    return render(request,'Books/author_index.html')

def Author_detail_view(request,pk):
    author = get_object_or_404(Author,pk=pk)
    context = {
        'author':author
    }
    return render(request,'Books/author_detail.html',context)

def User_create_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    form = UserForm()
    context = {
        'form' : form
    }
    return render(request,'Books/user_create.html',context)

def User_update_view(request,pk):
    user = get_object_or_404(User,pk=pk)
    form = UserForm(request.POST or None,instance=user)
    if form.is_valid():
        form.save()
        return redirect(reverse('books:user_list_view'))
    context={
        'form':form
    }
    return render(request,'Books/user_update.html',context)

def User_delete_view(request,pk):
    user=get_object_or_404(User,pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect(reverse('books:user_list_view'))
    context = {
        'user': user
    }
    return render(request,'Books/user_delete.html',context)

def User_list_view(request):
    user = User.objects.all()
    context = {
        'user':user
    }
    return render(request,"Books/user_list_view.html",context)

def User_index_view(request):
    user = User.objects.all()
    context = {
        'user':user
    }
    return render(request,'Books/user_index.html',context)

def User_detail_view(request,pk):
    user=get_object_or_404(User,pk=pk)
    books = user.books.all()
    context={
        'user':user,
        'books':books
    }
    return render(request,'Books/user_detail.html',context)

def Book_issue_view(request):
    if request.method == 'GET':
        books_list = Books.objects.all()
        users_list = User.objects.all()
        context = {
            'books_list':books_list,
            'users_list':users_list
        }
    else:
        book_pk = request.POST.get('books_pk')
        user_pk = request.POST.get('users_pk')
        book = Books.objects.get(pk = book_pk)
        user = User.objects.get(pk = user_pk)

        user.books.add(book)
        user.no_of_books_taken+=1
        user.save()
        #send mail
        subject = 'Book issue by library'
        message = f'Book name is {book.name}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['pragati.shah87@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )    
        return redirect(reverse('books:user_detail_view', args = [user_pk]))

    return render(request,'Books/book_issue.html',context)

def Book_return_view(request,pk):
    user=get_object_or_404(User,pk=pk)
    if request.method == 'GET':
        books_list = user.books.all()
        context = {
            'books_list':books_list,
        }
    else:
        book_pk = request.POST.get('books_pk')
        book = Books.objects.get(pk = book_pk)
        user.books.remove(book)
        user.no_of_books_taken-=1
        user.save()
        return redirect(reverse('books:user_detail_view', args = [pk]))

    return render(request,'books/book_return.html',context)

def Book_return_user(request):
    users_list = User.objects.all()
    context = {
        'users_list':users_list,
    }
    if request.method == 'POST':
        user_pk = request.POST.get('users_pk')
        return redirect(reverse('books:book_return_view', args = [user_pk]))
    return render(request,'books/book_return_user.html',context)


def Book_return1(request):
    user_pk = 1
    if request.method == 'GET':
        print("pragati",request.GET.get('users_pk'))
        if request.GET.get('users_pk') is not None:
            user_pk = request.GET.get('users_pk')
            print("hi",user_pk)
        print("hello",user_pk)
        user=get_object_or_404(User,pk=user_pk)
        books_list = user.books.all()
        users_list = User.objects.all()
        context = {
            'books_list':books_list,
            'users_list':users_list,
        }
    else:
        user_pk = request.POST.get('users_pk')
        user=get_object_or_404(User,pk=user_pk)
        book_pk = request.POST.get('books_pk')
        book = Books.objects.get(pk = book_pk)
        user.books.remove(book)
        user.no_of_books_taken-=1
        user.save()
        return redirect(reverse('books:user_detail_view', args = [user_pk]))

    return render(request,'books/book_return.html',context)

# def Book_return1(request):
#     users_list = User.objects.all()
#     context = {
#         'users_list':users_list,
#     }
#     if request.method == 'POST':
#         user_pk = request.POST.get('users_pk')
#         user=get_object_or_404(User,pk=user_pk)
#         books_list = user.books.all()
#         context = {
#         'books_list':books_list,
#         'users_list':users_list,
#         }
#         book_pk = request.POST.get('books_pk')
#         book = Books.objects.get(pk = book_pk)
#         user.books.remove(book)
#         user.no_of_books_taken-=1
#         user.save()
#         return redirect(reverse('books:user_detail_view', args = [user_pk]))

#     return render(request,'books/book_return.html',context)
