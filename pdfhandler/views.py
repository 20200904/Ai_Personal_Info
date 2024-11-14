# pdfhandler/views.py
from django.shortcuts import render

def main_page(request):
    return render(request, r'C:\Users\a\Desktop\프로젝트준비-2024.0\d\myproject\pdfhandler\templates\pdfhandler\main_page.html')
