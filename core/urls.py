from django.contrib import admin
from django.urls import path
from portal.views import home, especies, mapa, dados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('especies/', especies, name='especies'),
    path('mapa/', mapa, name='mapa'),
    path('dados/', dados, name='dados'),
]