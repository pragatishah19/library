from django.contrib import admin
from django.urls import path
from books.views import (
    Home_view,About,Contact_us,static_demo_view,Genre_create_view,Book_issue_view,Book_return_view,Book_return1,Book_return_user,
    Book_index_view,Book_list_view,Book_detail_view,Book_create_view,Book_update_view,Book_delete_view,
    Author_create_view,Author_list_view,Author_index_view,Author_delete_view,Author_detail_view,Author_update_view,
    User_list_view,User_index_view,User_detail_view,User_create_view,User_update_view,User_delete_view,
    BookDetailView,BookListView,AuthorDetailView,AuthorListView,BookCreateView,BookUpdateView,BookDeleteView
    )

app_name = 'books'

urlpatterns = [
    path('home/',Home_view,name = 'home'),
    path('about/',About,name = 'about'),
    path('contact/',Contact_us),
    path('static/',static_demo_view,name='static_demo_view'),
    path('genre_create/',Genre_create_view),
    path('issue/',Book_issue_view,name = 'book_issue_view'),
    path('user/<int:pk>/return/',Book_return_view,name = 'book_return_view'),
    path('user/return/',Book_return_user,name = 'book_return_user'),
    path('user/return/',Book_return1,name = 'book_return1'),

    # path('book_create/',Book_create_view),
    path('book_create/',BookCreateView.as_view(),name='book_create_view'),
#    path('book_list/', Book_list_view, name='book_list_view'),
    path('book_list1/', Book_list_view, name='book_list1_view'),
    path('book_list/', BookListView.as_view(), name='book_list_view'),
    path('book_index/', Book_index_view, name='book_index_view'),
#    path('<int:pk>/',Book_detail_view,name='book_detail_view'),
    path('<int:pk>/',BookDetailView.as_view(),name='book_detail_view'),
    # path('<int:pk>/update',Book_update_view,name='book_update_view'),
    path('<int:pk>/update',BookUpdateView.as_view(),name='book_update_view'),
    # path('<int:pk>/delete',Book_delete_view,name='book_delete_view'),
    path('<int:pk>/delete1',Book_delete_view,name='book_delete1_view'),
    path('<int:pk>/delete',BookDeleteView.as_view(),name='book_delete_view'),

    path('author_create/',Author_create_view,name='author_create_view'),
    # path('author_list/', Author_list_view, name='author_list_view'),
    path('author_list/',AuthorListView.as_view() , name='author_list_view'),
    path('author_index/',Author_index_view),
    # path('author/<int:pk>/',Author_detail_view,name='author_detail_view'),
    path('author/<int:pk>/',AuthorDetailView.as_view(),name='author_detail_view'),
    path('author/<int:pk>/update',Author_update_view,name='author_update_view'),
    path('author/<int:pk>/delete',Author_delete_view,name='author_delete_view'),

    path('user_create/',User_create_view,name='user_create_view'),
    path('user/<int:pk>/update',User_update_view,name='user_update_view'),
    path('user/<int:pk>/delete',User_delete_view,name='user_delete_view'),
    path('user_list/', User_list_view, name='user_list_view'),
    path('user_index/',User_index_view),
    path('user/<int:pk>/',User_detail_view,name='user_detail_view'),
]
