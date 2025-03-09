
from django.contrib import admin
from django.urls import path, include

from authentication.views import CustomTokenObtainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('simple_crud/', include('simple_crud.urls')),
    path("token/", CustomTokenObtainView.as_view()),
    path("token/refresh/", CustomTokenObtainView.as_view())
]
