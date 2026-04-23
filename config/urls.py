from django.contrib import admin
from django.urls import path, include # include сөзсүз болушу керек

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), # 'main' колдонмосун проектке коштук
]