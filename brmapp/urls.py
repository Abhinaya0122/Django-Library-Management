
from django.contrib import admin
from django.urls import path,include,re_path
from .views import aboutus, admin_borrow_list, admin_dashboard, admin_login_view, helloView,addBookView,addBook,editBook,editBookView,deleteBookView, indexview, landing, login_view, manage_book, borrow_book, my_borrowed_books, myborrow, returnbook
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",landing),
    path("admin_login/",admin_login_view),
    path('admin_dashboard/', admin_dashboard),
    path('manage-book/',manage_book),
    path("stud_login/",login_view),
    path("dashboard/",indexview),
    path("aboutus/",aboutus),
    path("view-book/",helloView),
    path("add-book/",addBookView),
    path("add-book/add",addBook),
    path("edit-book/",editBookView),
    path("edit-book/edit",editBook),
    path("delete-book",deleteBookView),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('borrow/',borrow_book),
    path('myborrow/',my_borrowed_books),
    path('return-book/',returnbook),
    path('admin-borrow-list/', admin_borrow_list),

]
