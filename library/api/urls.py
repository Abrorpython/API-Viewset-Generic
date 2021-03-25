from django.urls import path
from api import views

urlpatterns = [
    path('category-list/',views.BookCategoryListView.as_view()),
    path('category-create/',views.BookCategoryCreateView.as_view()),
    path('category-list-create/',views.BookCategoryListCreatView.as_view()),
    path('category-retry/<int:pk>',views.BookCategoryRetrieveView.as_view()),
    path('category-update/<int:pk>',views.BookCategoryUpdateView.as_view()),
    path('category-retrieve-update/<int:pk>',views.BookCategoryRetrieveUpdateView.as_view()),
    path('category-delete/<int:pk>',views.BookCategoryDestroyView.as_view()),
    path('category-list-delete/<int:pk>',views.BookCategoryDestroyView.as_view()),
]