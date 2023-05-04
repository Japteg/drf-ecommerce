from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include('demo.urls', namespace='demo')),
    path('api/', include('drf.urls')),
    path('search/', include('search.urls'))
]
