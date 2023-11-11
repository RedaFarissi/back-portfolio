from django.urls import path
from . import views 

urlpatterns = [ 
    path('create-contact/' , views.crate_contact ),
] 