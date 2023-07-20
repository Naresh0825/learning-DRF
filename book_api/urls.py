from django.urls import path

from . import views

urlpatterns =[
    path('create',views.BookCreate.as_view()), #localhost:8000/api/pk
    path('list/',views.BookList.as_view()), #localhost:8000/api/
    path('<int:pk>',views.BookById.as_view()), #localhost:8000/api/
    
]