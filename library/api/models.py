from django.db import models

class Book(models.Model):       # Book nomli Class yaratdim # PostgreSQLda table yaratiladi
    name = models.CharField(max_length=255,null=False,blank=False)  # Tbaleni polyalari

    def __str__(self):      # adminga qaysi polya ko'rinishini qaytaradi
        return self.name


class LibUser(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    def __str__(self):
        return self.name


class RentBook(models.Model):
    book = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(LibUser,on_delete=models.SET_NULL,null=True) # LibUserni ixtiyoriy tanlaymiz
    rendate = models.DateTimeField(auto_now_add=True)       # avtomatik vaqt qo'yadi
    returndDate = models.DateTimeField(null=True,blank=True)    # null vaqtni yozish shart emas, Blank Django yordamidan Vaqtni yozish shart emas

    def __str__(self):
        return '%s - %s' % (self.user,self.book)


class BookCategory(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    descriptions = models.TextField(null=False,blank=False)

    def __str__(self):
        return (self.name)