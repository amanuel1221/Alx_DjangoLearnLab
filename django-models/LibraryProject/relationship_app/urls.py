from django.urls import path
from .views import list_books, register, CustomLoginView, CustomLogoutView
from . import views

urlpatterns = [
    path("books/", list_books, name="list_books"),  # function-based view
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),  # class-based view
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
]
