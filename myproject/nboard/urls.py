from . import views
from django.urls import path

urlpatterns = [
    path('', views.NoticeBoard.as_view(), name='home'),
    path('<slug:slug>/', views.NoticeDetail.as_view(), name='notice_detail'),

]