from django.shortcuts import render
from rest_framework import viewsets, generics  # Django rest-frameworkdan viewsetni import qildim
from rest_framework.response import Response # Bizga ma'lumot qaytaradi

from .models import Book, LibUser, RentBook, BookCategory  # modelimdan classlarni import qildim
from .serializers import BookSerializer, LibUserSerializer, RentBookSerializer, \
    BookCategorySerializer  # serilaizers modulidan Yaratilgam serilaziers claslarni import qilyapman


class BookViewSet(viewsets.ViewSet):
    def list(self,request):     # GET zapros uchun
        queryset = Book.objects.all()  # Modelining Book clasidagi barchasini o'qiymiz
        serializers = BookSerializer(queryset,many=True)    # queryset o'zgaruvchisi yordamida BookSerializerga ma'lumotlarni serilazier o'zgaruvchisi yordamida uzatamaiz
        return Response(serializers.data)   # bizga Response yozrdamida barcha m'lumotlarni qaytaradi

    def post(self,request):     #POST zapros uchun
        serializers = BookSerializer(data=request.data)     # serializers o'zgaruvchisi yozrdamida Serilaizerdagi ma'lumotlarni to'dir
        if serializers.is_valid():          # agar ma'lumot to'g'ri to'ldirilgan bo'lsa
            serializers.save()              #  serilazers o'zgaruvchisiga saqla
            return Response(f"Qo'shildi >>> {serializers.data}")     # qaytaradi "Qo'shildi deb"
        return Response(f"Hatolik >>> {serializers.errors}")         # aks holda hatolik yuz beradi


# class BookViewSet(viewsets.ModelViewSet):   # viewset yaratdim
#     queryset = Book.objects.all()           # queryset yordamida Modeldagi biror clasni o'qiyman
#     serializer_class = BookSerializer       # serializer_class ushbu ozgaruvchiga Serializerdagi clasni o'zlashtirdim


class LibUserViewSet(viewsets.ModelViewSet):
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer


class RentBookViewSet(viewsets.ModelViewSet):
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer

#GET: SELECT
class BookCategoryListView(generics.ListAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

#POST: INSERT
class BookCategoryCreateView(generics.CreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

#GET and POST: SELECT and INSERT
class BookCategoryListCreatView(generics.ListCreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

#GET bitta api ni o'qish uchun class yozilmoqda
class BookCategoryRetrieveView(generics.RetrieveAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

#PUT: UPDATE
class BookCategoryUpdateView(generics.UpdateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

# GET and PUT: SELECT and UPDATE
class BookCategoryRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

#DELETE
class BookCategoryDestroyView(generics.DestroyAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

# GET and DELETE
class BookCategoryListDestroyView(generics.RetrieveDestroyAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer