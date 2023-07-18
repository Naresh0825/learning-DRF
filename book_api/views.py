from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from book_api.models import Book
from book_api.serializer import BookSerializer

# Create your views here.

@api_view(['GET'])
def books_list(request):
    books=Book.objects.all() #Complex Data
    serializer = BookSerializer(books,many=True) # Python Data Structure

    return Response(serializer.data )


@api_view(['POST'])
def books_create(request):
    serializer = BookSerializer(data=request.data) # Python Data Structure
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         
@api_view(['Get',"PUT","DELETE"])
def books_by_id(request,pk):
    try: # Python Data Structure
        books=Book.objects.get(pk=pk) #Complex Data
    except:
        return Response({"error":"Book does not exist"},status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer = BookSerializer(books) 
        return Response(serializer.data)
         
    if request.method=="PUT":
        serializer = BookSerializer(books,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    if request.method=="DELETE":
        books.delete() 
        return Response({"status":"Book Deleted Successfully"},status=status.HTTP_200_OK)
    
