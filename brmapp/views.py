from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .models import Book
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages

def admin_login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff:  
                login(request, user)
                return redirect('/admin_dashboard')  # Your custom admin page
            else:
                messages.error(request, "You are not authorized to access admin.")
    return render(request, 'admin_login.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, '/dashboard')

def admin_dashboard(request):
    return render(request,"admindashboard.html")

def landing(request):
    return render(request,'landing.html')


def indexview(request):
    return render(request,"home.html")

def landingview(request):
    return render(request,"landing.html")

def helloView(request):
    books=Book.objects.all()
    for book in books:
        print(book.availability)
    return render(request,"viewbook.html",{"books":books})

def aboutus(request):
    return render(request,"about.html")

def addBookView(request):
    return render(request,"addbook.html")

def manage_book(request):
    books=Book.objects.all()
    for book in books:
        print(book.availability)
    return render(request,"managebook.html",{"books":books})


def addBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        url = request.POST["image"]
        author = request.POST["author"]
        available = request.POST["available"]
        print(t,p,url)
        book=Book()
        book.title=t
        book.price=p
        book.image_url = url
        book.author=author
        book.availability=available
        book.save()
        return HttpResponseRedirect('/admin_dashboard')

def editBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        
        book=Book.objects.get(id=request.POST['bid'])
        book.title=t
        book.price=p
        book.save()
        return HttpResponseRedirect('/')


def editBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    print(book)
    return render(request,"edit-book.html",{"book":book})

def deleteBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/')