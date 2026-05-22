from django.contrib import admin
from django.urls import path, include
from backend.apps.notes.api import api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include("apps.notes.urls")),
    path('accounts/', include("apps.accounts.urls")),
    path('api/', api.urls)
]
