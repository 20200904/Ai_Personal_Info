# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views  # 현재 폴더(myproject)의 views.py를 임포트

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main_page'),  # 메인 페이지 URL 설정
    path('pdf/', include('pdf_processor.urls')),  # pdf_processor 앱의 URL 연결
]
