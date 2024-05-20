from django.urls import path
from .views import getYtURL,download_confirm,sample_download

urlpatterns = [
    path('', getYtURL, name="home"),
    path('download', download_confirm, name="download_confirm"),
    path('test', sample_download, name="sample"),

]
