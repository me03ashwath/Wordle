from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', include('login_signup.urls')),
    path('game/', include('game.urls')),
    # path('stats/', include('stats.urls')),
]