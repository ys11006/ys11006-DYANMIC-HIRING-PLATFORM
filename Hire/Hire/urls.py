from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import view
urlpatterns = [
     path('', view.home),
    path('admin/', admin.site.urls),
    path('',include('authuser.urls')),
    path('',include('candidate.urls')),
    path('',include('hr.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 