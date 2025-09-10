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

