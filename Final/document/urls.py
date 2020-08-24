from django.contrib import admin
from django.urls import path
from . import views

app_name = 'document'

urlpatterns = [
    path('', views.document, name='document'),
    path('document/<int:document_id>', views.document_detail, name="document_detail"),
]