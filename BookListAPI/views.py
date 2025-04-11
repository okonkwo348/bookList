from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from django.http import HttpResponseRedirect
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@api_view(['GET'])
def user_info(request):
    if request.user.is_authenticated:
        user=request.user
        token, created=Token.objects.get_or_create(user=user)
        return Response({
            'username':user.username,
            'email':user.email,
            'token':token.key
        })
    return HttpResponseRedirect('/api-auth/login/')


    
class BookList(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookDetail(generics.RetrieveDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer




# @api_view(['GET','POST'])
# def books(request):
#     return Response('List of the book', status=status.HTTP_200_OK)

# class BookList(APIView):
#     # def get(self,request):
#     #     return Response({"message":"List of the books"},status.HTTP_200_OK)

#     # To get book by author's name

#       def get(self,request):
#          author=request.GET.get('author')
#          if(author):
#             return Response({"message":"List of the books by" + author},status.HTTP_200_OK)
#          return Response ({"message":"list of the books"}, status.HTTP_200_OK)

#       def post(self,request):
#           return Response({"title":request.data.get("title")}, status.HTTP_201_CREATED)

# # get single title and name of author using primary key
# class Book(APIView):
#     def get(self, request,pk):
#         return Response({"message":"single book with id" + str(pk)}, status.HTTP_200_OK)

#     def put(self,request,pk):
#         return Response({"title":request.data.get('title')}, status.HTTP_200_OK)
