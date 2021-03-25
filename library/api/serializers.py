from rest_framework import serializers  # Django-rest frameworkdan serializers clasini import qilyapman
from .models import Book, LibUser, RentBook, BookCategory  # model modulidan claslarni import qilyapman


class BookSerializer(serializers.ModelSerializer): # Ma'lumotlar bazasidagi tabellarimdegi ma'lumotlarni API ko'rinisgiga o'tkazadi

    class Meta:             # Meta clas Bazadagi qaysi polyalarini o'qishni ko'rsatib ketdim
        model = Book        # Modelimdegi Mavjud clasni o'zlashtiraman
        fields = '__all__'  # Modelda yaratilgan classlarni barcha polyalarini oq'ib oladi


class LibUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = LibUser
        fields = '__all__'



class RentBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentBook
        fields = '__all__'


class BookCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BookCategory
        fields = '__all__'