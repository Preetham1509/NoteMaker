from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_home, name='note_home'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
]