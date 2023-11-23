from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BookView.as_view(), name=""),
    path("books/<int:pk>/", views.BookView.as_view(), name=""),
]
