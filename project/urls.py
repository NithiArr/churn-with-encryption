from django.contrib import admin
from django.urls import path
from login.views import loginn,registerr,register,logout
from base.views import home,store
from predict.views import predict
urlpatterns = [
    path('',loginn),
    path('registerr',registerr),
    path('register',register,name=''),
    path('logout/',logout),
    path('store/',store,name='store'),
    path('home/',home,name='home'),    
    path('predict/',predict,name='predict'),
    path('admin/', admin.site.urls),
]
