
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('website_django307.apps.public.urls')),
    path('accounts/', include('website_django307.apps.accounts.urls')),
]
