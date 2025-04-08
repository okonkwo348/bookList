from django.urls import path, re_path
from . import views

urlpatterns=[
    # path('book/',views.books),
      path('book/',views.BookList.as_view()),
      path('book/<int:pk>',views.BookDetail.as_view()),

]