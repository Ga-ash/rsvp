from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
