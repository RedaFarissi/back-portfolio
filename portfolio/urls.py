from django.contrib import admin
from django.urls import path , include , re_path
from connectWithFront.views import front

from django.views.generic import TemplateView   # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", front , name="front"),
    path('api/', include('api.urls')),    

    # Catch all other routes and serve React index.html
    # you can go to all route manualy 
    re_path(r'^(?:.*)/?$', TemplateView.as_view(template_name='index.html'), name='react_frontend'),
]
