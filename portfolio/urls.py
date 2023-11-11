from django.contrib import admin
from django.urls import path , include
from connectWithFront.views import front


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", front , name="front"),
    path('api/', include('api.urls')),    
]
