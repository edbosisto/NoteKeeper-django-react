from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.getNotes, name="all-notes"),
    path('notes/<int:id>/', views.getNote, name="view-note"),
    # path('notes/create', views.createNote, name="create-note"),
    # path('notes/update', views.updateNote, name="update-note"),
    # path('notes/delete', views.deleteNote, name="delete-note"),
]