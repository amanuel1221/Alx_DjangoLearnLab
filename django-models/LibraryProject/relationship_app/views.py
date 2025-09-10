from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from .models import Book
from django import forms

# Book form for add/edit
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]

# Add book view
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})

# Edit book view
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/edit_book.html", {"form": form, "book": book})

# Delete book view
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})
from django.contrib.auth.decorators import user_passes_test, login_required

# Admin view
@login_required
@user_passes_test(lambda u: hasattr(u, 'profile') and u.profile.role == 'Admin')
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

# Librarian view
@login_required
@user_passes_test(lambda u: hasattr(u, 'profile') and u.profile.role == 'Librarian')
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

# Member view
@login_required
@user_passes_test(lambda u: hasattr(u, 'profile') and u.profile.role == 'Member')
def member_view(request):
    return render(request, "relationship_app/member_view.html")
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# Function-based view
# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Custom login view (optional, can use LoginView directly)
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"

# Custom logout view (optional, can use LogoutView directly)
class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"
# Class-based view using DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

