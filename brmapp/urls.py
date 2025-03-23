
from django.contrib import admin
from django.urls import path,include,re_path
from .views import aboutus, helloView,addBookView,addBook,editBook,editBookView,deleteBookView, indexview

urlpatterns = [
    path("",indexview),
    path("aboutus/",aboutus),
    path("view-book/",helloView),
    path("add-book/",addBookView),
    path("add-book/add",addBook),
    path("edit-book/",editBookView),
    path("edit-book/edit",editBook),
    path("delete-book",deleteBookView)
]
