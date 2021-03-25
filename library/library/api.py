from rest_framework import routers   # django rest frameworkdan routerni import qilindi
from api import views                # api APP idan viewsni import qilindi
router = routers.DefaultRouter()     #
router.register(r'book',views.BookViewSet,basename='book')      # views yordamida Viewsda yozilgan clasga murojat qilinadi
router.register(r'lib-user',views.LibUserViewSet)
router.register(r'ren-book',views.RentBookViewSet)
