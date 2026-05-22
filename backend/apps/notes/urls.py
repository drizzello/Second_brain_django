from django.urls import path

from . import views

app_name = "notes"

urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.list_notes, name="list"),
    path("<int:pk>/", views.note_detail, name="note_detail"),
    path("new/", views.add_note, name="add_note"),
    path("<int:pk>/delete/", views.delete_note, name="delete_note"),
    path("<int:pk>/edit/", views.update_note, name="update_note"),
]
