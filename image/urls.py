from django.urls import path
from . import views

app_name = 'image'

urlpatterns = [

    path('',views.image_view, name = 'image'),  # 이전 - 홈화면
    path('convert/', views.image_convert , name='convert'), #컨버트한 화면


]