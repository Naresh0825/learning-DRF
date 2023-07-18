from django.urls import path

from . import views

urlpatterns =[
    path('',views.books_list), #localhost:8000/api/
    path('<int:pk>',views.books_by_id), #localhost:8000/api/
    path('create',views.books_create) #localhost:8000/api/pk
    
]