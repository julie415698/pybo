from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'chart'

urlpatterns = [


    path('', views.chart_view, name='chart'),  # 전체차트 -

    path('my_chart/', views.mychart_view, name='my_chart')    #사용자 차트


]