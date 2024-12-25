from django.urls import path
from . import views

app_name = "products"  # namespace 추가

urlpatterns = [
    path("", views.products, name="products"),  # 물건 목록 
    path("create", views.create, name="create"),  # 물건 목록에 등록 
    #
    path("index/", views.index, name="index"),
]